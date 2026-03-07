from src.character.enemy.enemy import EnemyBase, EnemyMedium, EnemyEasy


class EnemyFactory:
    @staticmethod
    def create_enemy(enemy_type: EnemyEasy | EnemyMedium) -> EnemyBase:
        return enemy_type
