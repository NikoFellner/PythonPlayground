from enum import StrEnum
from typing import Type

from pydantic import BaseModel

from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_easy import EnemyEasy
from src.character.enemy.enemy_medium import EnemyMedium


class EnemyType(StrEnum):
    EASY = "EnemyEasy"
    MEDIUM = "EnemyMedium"


class EnemyConfig(BaseModel):
    enemy_type: EnemyType


class EnemyMapping(dict):
    enemy_mapping: dict[EnemyType, Type[EnemyBase]]= {
        EnemyType.EASY: EnemyEasy,
        EnemyType.MEDIUM: EnemyMedium,
    }
