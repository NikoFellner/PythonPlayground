from src.character.base.base_character import BaseCharacter
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.character.enemy.enemy_type import EnemyConfig


class EnemyBase(BaseCharacter):
    def __init__(self, enemy_config: "EnemyConfig"):
        super().__init__()
        self._attack_power_level = enemy_config.enemy_stats.attack_power_level
        self._health_power_level = enemy_config.enemy_stats.health_power_level
        self._armor_power_level = enemy_config.enemy_stats.armor_power_level
        self._difficulty_power_level = enemy_config.enemy_stats.difficulty_power_level

    def attack(self) -> float:
        return (
            self.attack_power
            + self._attack_power_level * self._difficulty_power_level * 1.5
        )

    def defend(self) -> float:
        return self.armor + self._armor_power_level * self._difficulty_power_level * 2

    def heal(self) -> float:
        return (
            self._health + self._health_power_level * self._difficulty_power_level * 5
        )

    def _increase_attack_power_level(self, value: int) -> None:
        self._attack_power_level += value

    def _increase_health_power_level(self, value: int) -> None:
        self._health_power_level += value

    def _increase_armor_power_level(self, value: int) -> None:
        self._armor_power_level += value

    def _increase_difficulty_power_level(self, value: int) -> None:
        self._difficulty_power_level += value
