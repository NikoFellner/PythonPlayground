from src.character.enemy.enemy_factory import EnemyFactory
from src.character.enemy.enemy_type import EnemyConfig, EnemyType
from src.character.hero.hero import Hero
from src.character.hero.hero_type import HeroConfig, HeroType
from src.services.game_service import Game


def test_game_loop_runs_end_to_end_and_returns_summary():
    enemy_config = EnemyConfig(enemy_type=EnemyType.EASY)
    enemy_factory = EnemyFactory(enemy_config=enemy_config)
    hero = Hero.create_hero(HeroConfig(hero_type=HeroType.MAGE))
    game = Game(enemy_factory=enemy_factory, hero=hero)

    summary = game.game_loop()

    assert summary.hero_alive is False
    assert summary.levels_cleared == 1
    assert summary.final_hero_health <= 0
    assert enemy_config.enemy_stats.difficulty_power_level == 2
