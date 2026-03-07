from src.character.base.base_character import BaseCharacter


class Warrior(BaseCharacter):
    def __init__(self):
        super().__init__()
        self._health = 120
        self._armor = 20
        self.armor_class = 10

    def attack(self) -> int:
        return self.attack_power

    def defend(self) -> int:
        return self.armor

    def heal(self) -> int:
        return self._health + 5
