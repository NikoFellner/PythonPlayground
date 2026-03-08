from enum import StrEnum

from pydantic import BaseModel

from src.character.enemy.enemy_easy import EnemyEasy
from src.character.enemy.enemy_medium import EnemyMedium


class EnemyType(StrEnum):
    EASY = "EnemyEasy"
    MEDIUM = "EnemyMedium"


class EnemyConfig(BaseModel):
    enemy_type: EnemyType


class EnemyMapping(dict):
    enemy_mapping = {
        EnemyType.EASY: EnemyEasy,
        EnemyType.MEDIUM: EnemyMedium,
    }
