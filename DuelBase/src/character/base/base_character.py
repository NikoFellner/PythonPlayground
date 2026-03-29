from abc import ABC, abstractmethod

from src.character.hero.hero_type import HeroStats


class BaseCharacter(ABC):
    def __init__(self, stats:HeroStats):
        self.__stats = stats

    @property
    def health(self):
        return self.__stats.health

    @health.setter
    def health(self, health):
        self.__stats.health = health

    @property
    def armor(self):
        return self.__stats.armor

    @armor.setter
    def armor(self, armor):
        self._armor = armor

    @property
    def attack_power(self):
        return self._attack_power

    @attack_power.setter
    def attack_power(self, attack_power):
        self._attack_power = attack_power

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def heal(self):
        pass
