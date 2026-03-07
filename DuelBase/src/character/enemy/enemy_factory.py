from src.character.enemy.enemy import EnemyBase
from src.character.enemy.enemy_type import EnemyConfig, EnemyMapping


class EnemyFactory:
    @staticmethod
    def create_enemy(enemy_type: EnemyConfig) -> EnemyBase:
        enemy_instance = EnemyMapping.enemy_mapping[enemy_type.enemy_type]
        return enemy_instance()
