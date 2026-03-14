from src.character.enemy.enemy_factory import EnemyFactory
from src.character.enemy.enemy_type import EnemyConfig, EnemyType


def test_increase_difficulty_power():
    #arrange
    enemy_config = EnemyConfig(enemy_type=EnemyType.EASY)
    enemy_factory = EnemyFactory(enemy_config)
    #act
    enemy_factory.increase_difficulty_power(10)
    enemy_instance = enemy_factory.create_enemy(enemy_factory.enemy_config)

    assert enemy_instance.difficulty_power_level == 10

def test_increase_health_power():
    #arrange
    enemy_config = EnemyConfig(enemy_type=EnemyType.EASY)
    enemy_factory = EnemyFactory(enemy_config)
    #act
    enemy_factory.increase_health_power(10)
    enemy_instance = enemy_factory.create_enemy(enemy_factory.enemy_config)

    assert enemy_instance.health_power_level == 10

def test_increase_attack_power():
    #arrange
    enemy_config = EnemyConfig(enemy_type=EnemyType.EASY)
    enemy_factory = EnemyFactory(enemy_config)
    #act
    enemy_factory.increase_attack_power(10)
    enemy_instance = enemy_factory.create_enemy(enemy_factory.enemy_config)

    assert enemy_instance.attack_power_level == 10

def test_increase_armor_power():
    #arrange
    enemy_config = EnemyConfig(enemy_type=EnemyType.EASY)
    enemy_factory = EnemyFactory(enemy_config)
    #act
    enemy_factory.increase_armor_power(10)
    enemy_instance = enemy_factory.create_enemy(enemy_factory.enemy_config)

    assert enemy_instance.armor_power_level == 10

def test_change_enemy_type():
    enemy_type1 = EnemyType.EASY
    enemy_type2 = EnemyType.MEDIUM

    enemy_config = EnemyConfig(enemy_type=enemy_type1)
    enemy_factory = EnemyFactory(enemy_config)

    result_type1 = type(enemy_factory.create_enemy(enemy_factory.enemy_config))

    enemy_factory.change_enemy_type(enemy_type2)

    result_type2 = type(enemy_factory.create_enemy(enemy_factory.enemy_config))

    assert result_type1 != result_type2
    assert result_type1.__name__ == EnemyType.EASY
    assert result_type2.__name__ == EnemyType.MEDIUM