from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_type import EnemyConfig, EnemyMapping


class EnemyFactory:
    def __init__(self, enemy_config: EnemyConfig):
        self._enemy_config = enemy_config

    def create_enemy(self) -> EnemyBase:
        enemy_instance = EnemyMapping.enemy_mapping[self._enemy_config.enemy_type]
        return enemy_instance()
