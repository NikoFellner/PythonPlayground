from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_factory import EnemyFactory
from src.character.enemy.enemy_type import EnemyConfig, EnemyStats, EnemyType


class EnemySpawnService:
    def __init__(self, enemy_factory: EnemyFactory):
        self._level = 1
        self._difficulty = 1
        self._enemy_factory = enemy_factory
        self._enemy_type = EnemyType.EASY

    def spawn(self) -> EnemyBase:
        enemy_config = EnemyConfig(
            enemy_stats=EnemyStats(
                attack_power_level=self._level,
                health_power_level=self._level,
                armor_power_level=self._level,
                difficulty_power_level=self._difficulty,
            ),
            enemy_type=self._enemy_type,
        )

        return self._enemy_factory.create_enemy(enemy_config)


