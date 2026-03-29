from src.character.enemy.enemy_type import EnemyConfig, EnemyType
from src.character.hero.hero_type import HeroConfig, HeroType
from src.services.dependency_injection import DependencyInjection

if __name__ == "__main__":
    enemy_config = EnemyConfig(enemy_type=EnemyType.EASY)
    hero_config = HeroConfig(hero_type=HeroType.MAGE)
    di = DependencyInjection(enemy_config=enemy_config, hero_config=hero_config)

    game = di.game
    game.fight()
