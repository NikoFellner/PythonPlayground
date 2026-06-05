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

class GridEnvironment:
    def __init__(self):
        self._state = self.reset()
        self._player_position = None

    @staticmethod
    def reset() -> State:
        return State(x_pos=1, y_pos=1)

    @staticmethod
    def step(player_position, action: Action)-> tuple[int,int]:
        if action.action == GridAction.up:
            new_player_position = (player_position[0]-1,player_position[1])
        elif action.action == GridAction.down:
            new_player_position= (player_position[0]+1,player_position[1])
        elif action.action == GridAction.right:
            new_player_position= (player_position[0],player_position[1]+1)
        elif action.action == GridAction.left:
            new_player_position= (player_position[0],player_position[1]-1)
        return new_player_position

    @staticmethod
    def get_available_action(
        grid_shape: tuple[int, int], player_position: tuple[int, int]
    ) -> list[Action]:
        x_player = player_position[1]
        y_player = player_position[0]

        grid_width = grid_shape[1]
        grid_height = grid_shape[0]

        available_action: list[Action] = []

        if y_player > 1:
            available_action.append(Action(action=GridAction.up))

        if y_player < grid_height:
            available_action.append(Action(action=GridAction.down))

        if x_player > 1:
            available_action.append(Action(action=GridAction.left))

        if x_player < grid_width:
            available_action.append(Action(action=GridAction.right))
        return available_action

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
        self._player_position = self.get_player_position(grid_shape, final_position)
        grid_field_with_player_position = self.set_player_position(
            grid_field_with_final_position, self._player_position
        )
        return grid_field_with_player_position

    @staticmethod
    def print_grid(grid: ndarray) -> None:
        print(grid)
