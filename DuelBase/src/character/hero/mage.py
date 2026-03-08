from src.character.base.base_character import BaseCharacter


class Mage(BaseCharacter):
    def __init__(self):
        super().__init__()
        self._health = 80
        self._armor = 10
        self.armor_class = 20

    def attack(self) -> int:
        return self.attack_power * 2

    def defend(self) -> int:
        return self.armor * 0.5

    def heal(self) -> int:
        return self._health + 5
