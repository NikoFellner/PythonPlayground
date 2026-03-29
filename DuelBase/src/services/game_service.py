from src.character.base.base_character import BaseCharacter
from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_factory import EnemyFactory
from src.character.enemy.enemy_type import EnemyConfig
from loguru import logger

from src.services.game_dataclasses import FightResults, GameData, GameSummary


class Game:
    def __init__(
        self,
        enemy_factory: EnemyFactory,
        hero: BaseCharacter,
    ):
        self.enemy_factory = enemy_factory
        self.hero = hero

    @staticmethod
    def _fight(enemy: EnemyBase, hero: BaseCharacter) -> FightResults:
        while hero.health > 0:
            hero_dmg = hero.attack()
            logger.info(f"Hero dmg dealt:{hero_dmg}")
            logger.info(f"Enemy health: {enemy.health}")
            enemy.health -= hero_dmg
            if enemy.health <= 0:
                logger.info("You won this fight!")
                return FightResults(
                    hero_alive=True,
                    enemy_alive=False,
                    hero_health=hero.health,
                    enemy_health=enemy.health,
                )
            enemy_dmg = enemy.attack()
            hero.health -= enemy_dmg
            logger.info(f"Enemy dmg dealt: {enemy_dmg}")
            logger.info(f"Hero health: {hero.health}")

        return FightResults(
            hero_alive=False,
            enemy_alive=True,
            hero_health=hero.health,
            enemy_health=enemy.health,
        )

    def game_loop(self) -> GameSummary:
        game_data = GameData()
        while self.hero.health > 0:
            enemy = self.enemy_factory.create_enemy(self.enemy_factory.enemy_config)
            fight_result = self._fight(enemy=enemy, hero=self.hero)

            if not fight_result.hero_alive:
                return GameSummary(
                    levels_cleared=game_data.game_level - 1,
                    hero_alive=False,
                    final_hero_health=fight_result.hero_health,
                )
            game_data.game_level += 1
            self._scale_difficulty(self.enemy_factory.enemy_config)
            self.hero.heal()

        return GameSummary(
            levels_cleared=game_data.game_level - 1,
            hero_alive=False,
            final_hero_health=self.hero.health,
        )

    @staticmethod
    def _scale_difficulty(enemy_config: EnemyConfig) -> None:
        enemy_config.enemy_stats.difficulty_power_level += 1
