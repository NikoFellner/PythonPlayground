from src.character.enemy.enemy_factory import EnemyFactory
from src.character.enemy.enemy_type import EnemyConfig, EnemyType
from src.character.mage import Mage
from src.character.warrior import Warrior

if __name__ == "__main__":
    mage = Mage()
    warrior = Warrior()

    while True:
        print(f"Mage health: {mage.health}")
        print(f"Warrior healt: {warrior.health}")

        dmg = mage.attack()
        warrior.health -= dmg
        dmg = warrior.attack()
        mage.health -= dmg

        if mage.health <= 0 or warrior.health <= 0:
            break

        enemy_config = EnemyConfig(enemy_type=EnemyType.EASY)
        easy_enemy = EnemyFactory.create_enemy(enemy_config)
        enemy_config = EnemyConfig(enemy_type=EnemyType.MEDIUM)
        medium_enemy = EnemyFactory.create_enemy(enemy_config)
        print()
