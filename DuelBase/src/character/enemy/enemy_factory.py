from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_type import EnemyConfig, EnemyMapping, EnemyType


class EnemyFactory:
    def __init__(self, enemy_config: EnemyConfig):
        self.enemy_config = enemy_config

    @staticmethod
    def create_enemy(enemy_config: EnemyConfig) -> EnemyBase:
        enemy_instance = EnemyMapping.enemy_mapping[enemy_config.enemy_type]
        return enemy_instance(enemy_config)

    def increase_attack_power(self, attack_power_level: int) -> None:
        self.enemy_config.enemy_stats.attack_power_level = attack_power_level

    def increase_health_power(self, health_power_level: int) -> None:
        self.enemy_config.enemy_stats.health_power_level = health_power_level

    def increase_armor_power(self, armor_power_level: int) -> None:
        self.enemy_config.enemy_stats.armor_power_level = armor_power_level

    def increase_difficulty_power(self, difficulty_power_level: int) -> None:
        self.enemy_config.enemy_stats.difficulty_power_level = difficulty_power_level

    def change_enemy_type(self, enemy_type: EnemyType) -> None:
        self.enemy_config.enemy_type = enemy_type
