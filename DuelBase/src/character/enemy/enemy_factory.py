from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_type import EnemyConfig, EnemyMapping


class EnemyFactory:
    @staticmethod
    def create_enemy(enemy_config: EnemyConfig) -> EnemyBase:
        enemy_instance = EnemyMapping.enemy_mapping[enemy_config.enemy_type]
        return enemy_instance(enemy_config)
