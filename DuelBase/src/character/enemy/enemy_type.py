from enum import StrEnum
from typing import Type

from pydantic import BaseModel

from src.character.enemy.enemy_base import EnemyBase
from src.character.enemy.enemy_easy import EnemyEasy
from src.character.enemy.enemy_medium import EnemyMedium


class EnemyType(StrEnum):
    EASY = "EnemyEasy"
    MEDIUM = "EnemyMedium"


class EnemyStats(BaseModel):
    attack_power_level: int = 1
    health_power_level: int = 1
    armor_power_level: int = 1
    difficulty_power_level: int = 1


class EnemyConfig(BaseModel):
    enemy_type: EnemyType
    enemy_stats: EnemyStats = EnemyStats()


class EnemyMapping(dict):
    enemy_mapping: dict[EnemyType, Type[EnemyBase]] = {
        EnemyType.EASY: EnemyEasy,
        EnemyType.MEDIUM: EnemyMedium,
    }
