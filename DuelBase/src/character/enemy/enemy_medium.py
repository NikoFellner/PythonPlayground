from src.character.enemy.enemy_base import EnemyBase


class EnemyMedium(EnemyBase):
    def __init__(self):
        super().__init__()
        self._health = 40
        self._armor = 7
        self.attack_power = 10
