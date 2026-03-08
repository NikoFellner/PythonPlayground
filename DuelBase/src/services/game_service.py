from src.character.enemy.enemy_factory import EnemyFactory
from src.character.hero.hero import Hero
from src.services.user_interface import UserInterface


class Game:
    def __init__(self):
        self.ui = UserInterface()
        self.enemy_factory = EnemyFactory()
        self.hero_factory = Hero()
