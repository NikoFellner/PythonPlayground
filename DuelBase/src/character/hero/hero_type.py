from enum import StrEnum
from typing import Type

from pydantic import BaseModel

from src.character.base.character_stats import HeroStats
from src.character.base.base_character import BaseCharacter
from src.character.hero.mage import Mage
from src.character.hero.warrior import Warrior

class HeroLevel(BaseModel):
    xp: int = 0
    xp_to_next_level: int = 100
    current_level: int = 1

class HeroType(StrEnum):
    MAGE = "MageHero"
    WARRIOR = "WarriorHero"

class MageHeroStats:
    stats = HeroStats(health = 80,
    physical_defense = 10,
    magical_defense = 30,
    strength = 10,
    intelligence = 30)

class WarriorHeroStats:
    stats = HeroStats(health = 120,
    physical_defense = 30,
    magical_defense = 5,
    strength = 30,
    intelligence = 5)

class HeroConfig(BaseModel):
    hero_type: HeroType
    hero_level: HeroLevel = HeroLevel()

class HeroMapping(dict):
    hero_type_mapping: dict[HeroType, Type[BaseCharacter]] = {
        HeroType.MAGE: Mage,
        HeroType.WARRIOR: Warrior,
    }

    hero_stats_mapping: dict[HeroType, HeroStats] = {
        HeroType.MAGE: MageHeroStats.stats,
        HeroType.WARRIOR: WarriorHeroStats.stats,
    }
