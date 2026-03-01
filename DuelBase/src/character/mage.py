from src.character.base.base_character import BaseCharacter


class Mage(BaseCharacter):
    def attack(self) -> int:
        return self.attack_power * 2

    def defend(self) -> int:
        return self.armor * 0.5

    def heal(self) -> int:
        return self._health + 5
