from abc import ABC, abstractmethod

from src.character.base.character_stats import HeroStats


class BaseCharacter(ABC):
    def __init__(self, stats: HeroStats | None = None):
        self._stats = stats

    @property
    def health(self):
        if self._stats is not None:
            return self._stats.health
        return self._health

    @health.setter
    def health(self, health):
        if self._stats is not None:
            self._stats.health = health
            return
        self._health = health

    @property
    def armor(self):
        if self._stats is not None:
            return self._stats.physical_defense
        return self._armor

    @armor.setter
    def armor(self, armor):
        if self._stats is not None:
            self._stats.physical_defense = armor
            return
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
