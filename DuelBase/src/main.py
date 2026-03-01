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
