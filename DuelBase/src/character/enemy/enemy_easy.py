from src.character.enemy.enemy_base import EnemyBase


class EnemyEasy(EnemyBase):
    def __init__(self):
        super().__init__()
        self._health = 20
        self._armor = 3
        self.attack_power = 3
