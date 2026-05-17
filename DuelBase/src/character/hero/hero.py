from copy import deepcopy

from src.character.base.base_character import BaseCharacter
from src.character.hero.hero_type import HeroConfig, HeroMapping


class Hero:
    @staticmethod
    def create_hero(hero_config: HeroConfig) -> BaseCharacter:
        hero_instance = HeroMapping.hero_type_mapping[hero_config.hero_type]
        hero_stats = HeroMapping.hero_stats_mapping[hero_config.hero_type]
        return hero_instance(deepcopy(hero_stats))
