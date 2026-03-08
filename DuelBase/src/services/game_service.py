from src.character.base.base_character import BaseCharacter
from src.character.enemy.enemy_factory import EnemyFactory


class Game:
    def __init__(
        self,
        enemy_factory: EnemyFactory,
        hero: BaseCharacter,
    ):
        self.enemy_factory = enemy_factory
        self.hero_factory = hero
