import random
from enum import Enum

import numpy as np
from numpy import ndarray
from pydantic import BaseModel


class GridAction(str, Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


class Action(BaseModel):
    action: GridAction


class State(BaseModel):
    x_pos: int
    y_pos: int


class GridCoordniate(BaseModel):
    x_pos: int
    y_pos: int

    @property
    def position(self) -> tuple[int, int]:
        return (self.x_pos, self.y_pos)


class GridEnvironment:
    def __init__(self):
        self._state = self.reset()

    @staticmethod
    def reset() -> State:
        return State(x_pos=0, y_pos=0)

    def step(self, action: Action):
        pass

    def get_available_action(self):
        pass

    @staticmethod
    def create_grid(width: int, height: int) -> tuple[ndarray, tuple[int, int]]:
        return np.zeros(shape=(height, width)), (height, width)

    @staticmethod
    def get_final_position(grid_shape: tuple[int, int]) -> tuple[int, int]:
        # positions are handled starting from 1 to n
        x_pos = random.randint(1, grid_shape[0])
        y_pos = random.randint(1, grid_shape[1])
        final_position = (x_pos, y_pos)
        return final_position

    @staticmethod
    def set_final_positon(
        grid_field: ndarray, final_position: tuple[int, int]
    ) -> ndarray:
        grid_field[final_position[0] - 1][final_position[1] - 1] = 1
        return grid_field

    @staticmethod
    def get_player_position(
        grid_shape: tuple[int, int], final_position: tuple[int, int]
    ) -> tuple[int, int]:
        while True:
            x_pos = random.randint(1, grid_shape[1] - 1)
            y_pos = random.randint(1, grid_shape[0] - 1)
            if not (x_pos, y_pos) == final_position:
                break
        return (x_pos, y_pos)

    @staticmethod
    def set_player_position(
        grid_field: ndarray, player_position: tuple[int, int]
    ) -> ndarray:
        grid_field[player_position[0] - 1][player_position[1] - 1] = 2
        return grid_field

    def create_env(self) -> ndarray:
        grid_field, grid_shape = self.create_grid(5, 5)
        final_position = self.get_final_position(grid_shape)
        grid_field_with_final_position = self.set_final_positon(
            grid_field, final_position
        )
        player_position = self.get_player_position(grid_shape, final_position)
        grid_field_with_player_position = self.set_player_position(
            grid_field_with_final_position, player_position
        )
        return grid_field_with_player_position

    @staticmethod
    def print_grid(grid:ndarray)->None:
        print(grid)