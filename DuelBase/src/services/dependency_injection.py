from src.character.base.base_character import BaseCharacter
from src.character.enemy.enemy_factory import EnemyFactory
from src.character.enemy.enemy_type import EnemyConfig
from src.character.hero.hero import Hero
from src.character.hero.hero_type import HeroConfig
from src.services.game_service import Game


class DependencyInjection:
    def __init__(self, hero_config: HeroConfig, enemy_config: EnemyConfig):
        self.hero_config = hero_config
        self.enemy_config = enemy_config

        self.__hero = self._create_hero(hero_config)
        self.__enemy_factory = self._create_enemy_factory(enemy_config)

    @property
    def hero(self) -> BaseCharacter:
        return self.__hero

    @property
    def enemy_factory(self) -> EnemyFactory:
        return self.__enemy_factory

    @property
    def game(self):
        return Game(hero=self.hero, enemy_factory=self.enemy_factory)

    @staticmethod
    def _create_hero(hero_config: HeroConfig) -> BaseCharacter:
        return Hero.create_hero(hero_config)

    @staticmethod
    def _create_enemy_factory(enemy_config: EnemyConfig) -> EnemyFactory:
        return EnemyFactory(enemy_config)
