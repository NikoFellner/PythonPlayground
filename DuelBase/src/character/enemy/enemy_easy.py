from src.character.enemy.enemy_base import EnemyBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.character.enemy.enemy_type import EnemyConfig


class EnemyEasy(EnemyBase):
    def __init__(self, enemy_config: "EnemyConfig"):
        super().__init__(enemy_config)
        self._health = 20
        self._armor = 3
        self.attack_power = 3
