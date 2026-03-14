from src.character.base.base_character import BaseCharacter
from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_factory import EnemyFactory
from src.character.enemy.enemy_type import EnemyConfig
from loguru import logger

from src.messaging.messages_exceptions import HeroDied


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

    def fight(self):
        while self.hero.health > 0:
            enemy_instance = self.enemy_factory.create_enemy(
                self.enemy_factory.enemy_config
            )
            self.hero = Game._fight(enemy=enemy_instance, hero=self.hero)
            self.enemy_factory.increase_health_power(5)
            self.hero.heal()

    @staticmethod
    def _fight(enemy: EnemyBase, hero: BaseCharacter):
        while enemy.health > 0 and hero.health > 0:
            hero_dmg = hero.attack()
            logger.info(f"Hero dmg dealt:{hero_dmg}")
            logger.info(f"Enemy health: {enemy.health}")
            enemy.health -= hero_dmg
            if enemy.health <= 0:
                logger.info("You won this fight!")
                return hero

            enemy_dmg = enemy.attack()
            hero.health -= enemy_dmg
            logger.info(f"Enemy dmg dealt: {enemy_dmg}")
            logger.info(f"Hero health: {hero.health}")
            if hero.health <= 0:
                Game.game_over()

    @staticmethod
    def game_over():
        logger.info("Game over")
        raise HeroDied()
