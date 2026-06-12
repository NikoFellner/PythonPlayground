from enum import Enum

from pydantic import BaseModel


class GridAction(str, Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


class Action(BaseModel):
    action: GridAction


class Grid(BaseModel):
    width: int
    height: int

    @property
    def shape(self) -> tuple[int, int]:
        return self.height, self.width


class State(BaseModel):
    row_pos: int
    column_pos: int


class Reward(BaseModel):
    reward: float


class Goal(BaseModel):
    reached: bool
