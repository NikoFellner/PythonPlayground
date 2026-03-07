from enum import StrEnum

from pydantic import BaseModel

from src.character.enemy.enemy import EnemyEasy, EnemyMedium


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
