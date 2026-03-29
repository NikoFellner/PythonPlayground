from src.character.base.base_character import BaseCharacter
from src.character.hero.hero_type import HeroStats


class Warrior(BaseCharacter):
    def __init__(self, stats:HeroStats):
        super().__init__(stats)


    def attack(self) -> int:
        return self.__stats.strength * 2

    def defend(self) -> float:
        return self.__stats.physical_defense * 0.5

    def heal(self) -> None:
        self.__stats.health += 5
