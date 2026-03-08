from enum import StrEnum

from pydantic import BaseModel

from src.character.hero.mage import Mage
from src.character.hero.warrior import Warrior


class HeroType(StrEnum):
    MAGE = "MageHero"
    WARRIOR = "WarriorHero"


class HeroConfig(BaseModel):
    hero_type: HeroType


class HeroMapping(dict):
    hero_mapping = {
        HeroType.MAGE: Mage,
        HeroType.WARRIOR: Warrior,
    }
