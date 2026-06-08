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


class Grid(BaseModel):
    width: int
    height: int

    @property
    def shape(self) -> tuple[int, int]:
        return self.height, self.width


class State(BaseModel):
    row_pos: int
    column_pos: int


class GridEnvironment:
    def __init__(self, width: int = 5, height: int = 5):
        self._width = width
        self._height = height
        self.reset()

    def reset(self) -> None:
        self._env, self._grid = self.create_grid(self._width, self._height)
        self._final_position: State = self.get_final_position(self._grid)
        self._player_position: State = self.get_player_position(
            self._grid, self._final_position
        )
        self._env = self.set_final_positon(self._env, self._final_position)
        self._env = self.set_player_position(self._env, self._player_position)

    @staticmethod
    def suqared_difference(value_1: int, value_2: int) -> float:
        return np.square(value_2 - value_1)

    @staticmethod
    def euclidean_distance(point_1: State, point_2: State):
        column_sq_diff = GridEnvironment.suqared_difference(
            point_1.column_pos, point_2.column_pos
        )
        row_sq_diff = GridEnvironment.suqared_difference(
            point_1.row_pos, point_2.row_pos
        )
        return np.sqrt(column_sq_diff + row_sq_diff)

    def step(
        self,
        action: Action,
    ) -> tuple[State, float, bool]:
        player_position = self._player_position
        player_row = player_position.row_pos
        player_col = player_position.column_pos

        if action.action == GridAction.up:
            player_row -= 1
        elif action.action == GridAction.down:
            player_row += 1
        elif action.action == GridAction.right:
            player_col += 1
        elif action.action == GridAction.left:
            player_col -= 1

        player_new_position = State(row_pos=player_row, column_pos=player_col)
        reward = -0.1
        if player_new_position == self._final_position:
            goal_reached = True
            reward += 1
        else:
            goal_reached = False
            reward -= 1

        self._player_position = player_new_position
        return player_new_position, reward, goal_reached

    @staticmethod
    def get_available_actions(grid_shape: Grid, player_position: State) -> list[Action]:
        row_player = player_position.row_pos
        column_player = player_position.column_pos

        grid_width = grid_shape.width
        grid_height = grid_shape.height

        available_action: list[Action] = []

        if column_player > 1:
            available_action.append(Action(action=GridAction.up))

        if column_player < grid_height:
            available_action.append(Action(action=GridAction.down))

        if row_player > 1:
            available_action.append(Action(action=GridAction.left))

        if row_player < grid_width:
            available_action.append(Action(action=GridAction.right))
        return available_action

    @staticmethod
    def create_grid(width: int, height: int) -> tuple[ndarray, Grid]:
        return np.zeros(shape=(height, width)), Grid(height=height, width=width)

    @staticmethod
    def get_final_position(grid_shape: Grid) -> State:
        # positions are handled starting from 1 to n
        row_pos = random.randint(1, grid_shape.width)
        column_pos = random.randint(1, grid_shape.height)
        final_position = State(row_pos=row_pos, column_pos=column_pos)
        return final_position

    @staticmethod
    def set_final_positon(grid_field: ndarray, final_position: State) -> ndarray:
        grid_field[final_position.column_pos - 1][final_position.row_pos - 1] = 1
        return grid_field

    @staticmethod
    def get_player_position(grid_shape: Grid, final_position: State) -> State:
        while True:
            row_pos = random.randint(1, grid_shape.height)
            column_pos = random.randint(1, grid_shape.width)
            if not State(row_pos=row_pos, column_pos=column_pos) == final_position:
                break
        return State(row_pos=row_pos, column_pos=column_pos)

    @staticmethod
    def set_player_position(grid_field: ndarray, player_position: State) -> ndarray:
        grid_field[player_position.column_pos - 1][player_position.row_pos - 1] = 2
        return grid_field

    def create_env(self) -> ndarray:
        grid_field, grid_shape = self.create_grid(5, 5)
        self._final_position = self.get_final_position(grid_shape)
        grid_field_with_final_position = self.set_final_positon(
            grid_field, self._final_position
        )
        self._player_position = self.get_player_position(
            grid_shape, self._final_position
        )
        grid_field_with_player_position = self.set_player_position(
            grid_field_with_final_position, self._player_position
        )
        return grid_field_with_player_position

    @staticmethod
    def print_grid(grid: ndarray) -> None:
        print(grid)
