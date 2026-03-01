from abc import ABC, abstractmethod


class BaseCharacter(ABC):
    def __init__(self):
        self._health = 100
        self._attack_power = 1
        self._armor = 1

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def armor(self):
        return self._armor

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
