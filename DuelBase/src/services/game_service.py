from src.character.base.base_character import BaseCharacter
from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_factory import EnemyFactory
from src.character.enemy.enemy_type import EnemyConfig
from loguru import logger

from src.messaging.messages_exceptions import HeroDied
from src.services.game_dataclasses import FightResults, GameData


class Game:
    def __init__(
        self,
        enemy_factory: EnemyFactory,
        hero: BaseCharacter,
        enemy_config: EnemyConfig,
    ):
        self.enemy_factory = enemy_factory
        self.hero = hero
        self.enemy_config = enemy_config

    def fight(self, game_data:GameData) -> tuple[GameData, FightResults]:
        enemy_instance = self.enemy_factory.create_enemy(
            self.enemy_factory.enemy_config
        )
        self.hero, _enemy, fight_results = Game._fight(enemy=enemy_instance, hero=self.hero)
        if fight_results.hero_alive:
            self.enemy_factory.increase_health_power(5)
            self.hero.heal()
        elif fight_results.enemy_alive:
            self.game_over()
        game_data.game_level +=1
        return game_data, fight_results

    @staticmethod
    def _fight(
        enemy: EnemyBase, hero: BaseCharacter
    ) -> tuple[BaseCharacter, EnemyBase, FightResults] | None:
        while enemy.health > 0 and hero.health > 0:
            hero_dmg = hero.attack()
            logger.info(f"Hero dmg dealt:{hero_dmg}")
            logger.info(f"Enemy health: {enemy.health}")
            enemy.health -= hero_dmg
            if enemy.health <= 0:
                logger.info("You won this fight!")
                return hero, enemy, FightResults(hero_alive=True, enemy_alive=False, hero_health=hero.health, enemy_health=enemy.health)
            enemy_dmg = enemy.attack()
            hero.health -= enemy_dmg
            logger.info(f"Enemy dmg dealt: {enemy_dmg}")
            logger.info(f"Hero health: {hero.health}")
            if hero.health <= 0:
                return hero, enemy,FightResults(hero_alive=False, enemy_alive=True, hero_health=hero.health, enemy_health=enemy.health)

    @staticmethod
    def game_over():
        logger.info("Game over")
        raise HeroDied()

    def game_loop(self):
        game_data = GameData()
        while self.hero.health > 0:
            game_data, fight_results = self.fight(game_data)
            logger.info(f"Hero health: {fight_results.hero_health}")