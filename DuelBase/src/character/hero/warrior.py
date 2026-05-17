from src.character.base.base_character import BaseCharacter
from src.character.base.character_stats import HeroStats


class Warrior(BaseCharacter):
    def __init__(self, stats: HeroStats):
        super().__init__(stats)


    def attack(self) -> int:
        return self._stats.strength * 2

    def defend(self) -> float:
        return self._stats.physical_defense * 0.5

    def heal(self) -> None:
        self._stats.health += 5
