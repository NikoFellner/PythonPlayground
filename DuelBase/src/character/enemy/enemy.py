from src.character.base.base_character import BaseCharacter


class EnemyBase(BaseCharacter):
    def attack(self) -> int:
        return self.attack_power

    def defend(self) -> int:
        return self.armor

    def heal(self) -> int:
        return self._health


class EnemyEasy(EnemyBase):
    def __init__(self):
        super().__init__()
        self._health = 20
        self._armor = 3
        self.attack_power = 3


class EnemyMedium(EnemyBase):
    def __init__(self):
        super().__init__()
        self._health = 40
        self._armor = 7
        self.attack_power = 10
