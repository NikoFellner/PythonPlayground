from enum import StrEnum

from pydantic import BaseModel


class ENEMY_CLASSES(StrEnum):
    EASY_ENEMY = "EnemyEasy"
    MEDIUM_ENEMY = "EnemyMedium"


class ENEMY(BaseModel):
    enemy_type: ENEMY_CLASSES
