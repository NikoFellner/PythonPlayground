
from src.character.enemy.enemy_type import EnemyConfig, EnemyType, EnemyStats
from src.character.hero.hero_type import HeroConfig, HeroType
from src.services.dependency_injection import DependencyInjection


def test_game_fight_hero_wins():
    enemy_stats = EnemyStats()
    enemy_stats.attack_power_level = 0
    enemy_config = EnemyConfig(enemy_type=EnemyType.EASY, enemy_stats=enemy_stats)
    hero_config = HeroConfig(hero_type=HeroType.MAGE)

    di = DependencyInjection(enemy_config=enemy_config, hero_config=hero_config)

    game = di.game
    enemy = di.enemy_factory.create_enemy(enemy_config)
    hero = di.hero
    fight_result = game._fight(enemy=enemy, hero=hero)
    assert fight_result.hero_health == 53
    assert fight_result.enemy_health <= 0
    assert fight_result.hero_alive == True
    assert fight_result.enemy_alive == False


def test_game_fight_hero_looses():
    enemy_stats = EnemyStats()
    enemy_stats.attack_power_level = 1000000
    enemy_config = EnemyConfig(enemy_type=EnemyType.EASY, enemy_stats=enemy_stats)
    hero_config = HeroConfig(hero_type=HeroType.MAGE)

    di = DependencyInjection(enemy_config=enemy_config, hero_config=hero_config)

    game = di.game
    enemy = di.enemy_factory.create_enemy(enemy_config)
    hero = di.hero
    fight_result = game._fight(enemy=enemy, hero=hero)
    assert fight_result.hero_health <=0
    assert fight_result.enemy_health > 0
    assert fight_result.hero_alive == False
    assert fight_result.enemy_alive == True
