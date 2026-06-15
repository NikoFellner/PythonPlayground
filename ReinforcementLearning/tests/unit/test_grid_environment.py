import numpy as np

from src.environment.grid_environment import GridEnvironment
from src.overarching.dependency_injection import DI
from src.overarching.schemas import GridAction, Action, State, Grid


def test_grid_base_clases():
    grid_action = GridAction.up
    action = Action(action=grid_action)
    grid_action_2 = GridAction.left
    assert action.action == "up"
    action = Action(action=grid_action_2)
    assert action.action == "left"


def test_grid_actions():
    assert GridAction.up == "up"
    assert GridAction.down == "down"
    assert GridAction.left == "left"
    assert GridAction.right == "right"


def test_reset_returns_a_state_value():
    env = DI.env

    player_state = env._player_position
    env.reset()
    player_state_2 = env._player_position

    assert type(player_state) is State
    assert type(player_state_2) is State
    assert player_state is not player_state_2


def test_get_final_position():
    grid_shape = Grid(height=3, width=3)
    final_positon = GridEnvironment.get_final_position(grid_shape)
    assert final_positon.row_pos <= 3
    assert final_positon.column_pos <= 3
    assert final_positon.row_pos > 0
    assert final_positon.column_pos > 0


def test_get_player_position():
    grid_shape = Grid(width=3, height=3)
    final_positon = State(row_pos=2, column_pos=1)
    player_position = GridEnvironment.get_player_position(grid_shape, final_positon)

    assert final_positon != player_position
    assert player_position.row_pos >= 1
    assert player_position.row_pos <= 3
    assert player_position.column_pos >= 1
    assert player_position.column_pos <= 3



def test_available_action_center():
    grid_shape = Grid(height=5, width=5)
    player_position = State(row_pos=2, column_pos=2)

    env = DI.env
    env._grid = grid_shape
    env._player_position = player_position

    available_actions = env.get_available_actions()

    assert len(available_actions) == 4
    assert Action(action=GridAction.right) in available_actions
    assert Action(action=GridAction.down) in available_actions
    assert Action(action=GridAction.left) in available_actions
    assert Action(action=GridAction.up) in available_actions


def test_available_action_left_upper_corner():
    grid_shape = Grid(height=5, width=5)
    player_position = State(row_pos=1, column_pos=1)

    env = DI.env
    env._grid = grid_shape
    env._player_position = player_position

    available_actions = env.get_available_actions()
    assert len(available_actions) == 2
    assert Action(action=GridAction.right) in available_actions
    assert Action(action=GridAction.down) in available_actions


def test_step_up():
    env = DI.env
    env._player_position = State(row_pos=2, column_pos=2)
    action = Action(action=GridAction.up)

    result_player_position, _, _ = env.step(action)

    expected_position = State(row_pos=2, column_pos=1)
    assert result_player_position == expected_position


def test_step_down():
    env = DI.env
    env._player_position = State(row_pos=2, column_pos=2)
    action = Action(action=GridAction.down)

    result_player_position, _, _ = env.step(action)

    expected_position = State(row_pos=2, column_pos=3)
    assert result_player_position == expected_position


def test_step_left():
    env = DI.env
    env._player_position = State(row_pos=2, column_pos=2)
    action = Action(action=GridAction.left)

    result_player_position, _, _ = env.step(action)

    expected_position = State(row_pos=1, column_pos=2)
    assert result_player_position == expected_position


def test_step_right():
    env = DI.env
    env._player_position = State(row_pos=2, column_pos=2)
    action = Action(action=GridAction.right)

    result_player_position, _, _ = env.step(action)

    expected_position = State(row_pos=3, column_pos=2)
    assert result_player_position == expected_position
