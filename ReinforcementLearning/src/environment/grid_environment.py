import random

from src.environment.environment import Environment
from src.overarching.config_schemas import EnvironmentConfig
from src.overarching.schemas import Action, State, GridAction, Grid, Reward, Goal


class GridEnvironment(Environment):
    def __init__(self, config: EnvironmentConfig):
        self._width = config.width
        self._height = config.height
        self._grid = Grid(height=self._height, width=self._width,)
        self.reset()

    def reset(self) -> None:
        self._final_position: State = self.get_final_position(self._grid)
        self._player_position: State = self.get_player_position(
            self._grid, self._final_position
        )

    @property
    def player_state(self) -> State:
        return self._player_position

    def step(
        self,
        action: Action,
    ) -> tuple[State, Reward, Goal]:
        player_position = self._player_position
        player_row = player_position.row_pos
        player_col = player_position.column_pos

        if action.action == GridAction.up:
            player_col -= 1
        elif action.action == GridAction.down:
            player_col += 1
        elif action.action == GridAction.right:
            player_row += 1
        elif action.action == GridAction.left:
            player_row -= 1

        player_new_position = State(row_pos=player_row, column_pos=player_col)
        reward = -0.1
        if player_new_position == self._final_position:
            goal_reached = True
            reward += 1
        else:
            goal_reached = False
            reward -= 1

        self._player_position = player_new_position
        return player_new_position, Reward(reward=reward), Goal(reached=goal_reached)

    def get_available_actions(self) -> list[Action]:
        available_action: list[Action] = GridEnvironment.available_actions_in_grid(
            self._player_position, self._grid
        )
        return available_action

    @staticmethod
    def available_actions_in_grid(state: State, grid: Grid) -> list[Action]:
        available_action: list[Action] = []
        column_state = state.column_pos
        row_state = state.row_pos

        grid_width = grid.width
        grid_height = grid.height

        if column_state > 1:
            available_action.append(Action(action=GridAction.up))

        if column_state < grid_height:
            available_action.append(Action(action=GridAction.down))

        if row_state > 1:
            available_action.append(Action(action=GridAction.left))

        if row_state < grid_width:
            available_action.append(Action(action=GridAction.right))
        return available_action


    @staticmethod
    def get_final_position(grid_shape: Grid) -> State:
        # positions are handled starting from 1 to n
        row_pos = random.randint(1, grid_shape.width)
        column_pos = random.randint(1, grid_shape.height)
        final_position = State(row_pos=row_pos, column_pos=column_pos)
        return final_position

    @staticmethod
    def get_player_position(grid_shape: Grid, final_position: State) -> State:
        while True:
            row_pos = random.randint(1, grid_shape.height)
            column_pos = random.randint(1, grid_shape.width)
            if not State(row_pos=row_pos, column_pos=column_pos) == final_position:
                break
        return State(row_pos=row_pos, column_pos=column_pos)