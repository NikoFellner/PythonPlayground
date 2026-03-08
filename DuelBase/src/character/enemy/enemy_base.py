from src.character.base.base_character import BaseCharacter


class EnemyBase(BaseCharacter):
    def attack(self) -> int:
        return self.attack_power

    def defend(self) -> int:
        return self.armor

    def heal(self) -> int:
        return self._health
