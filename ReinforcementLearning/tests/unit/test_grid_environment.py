import numpy as np

from src.environment.grid_environment import GridAction, Action, GridEnvironment, State


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
    env = GridEnvironment()

    state = env.reset()

    assert state is not None


def test_reset_returns_the_same_start_state_each_time():
    env = GridEnvironment()

    first_state = env.reset()
    second_state = env.reset()

    assert second_state == first_state


def test_reset_state_is_coordinate_like():
    env = GridEnvironment()

    state = env.reset()

    assert isinstance(state, State)
    assert len(state.model_dump()) == 2
    assert all(
        isinstance(state.model_dump()[value], int) for value in state.model_dump()
    )


def test_create_grid():
    grid_array, grid_shape = GridEnvironment.create_grid(3, 5)
    expected_array = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])

    assert np.array_equal(grid_array, expected_array)
    assert grid_shape == expected_array.shape


def test_create_asymmetric_grid():
    grid_array, grid_shape = GridEnvironment.create_grid(3, 3)
    expected_array = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    assert np.array_equal(grid_array, expected_array)
    assert grid_shape == expected_array.shape


def test_get_final_position():
    grid_shape = (3, 3)
    final_positon = GridEnvironment.get_final_position(grid_shape)
    assert final_positon[0] <= 3
    assert final_positon[1] <= 3
    assert final_positon[0] > 0
    assert final_positon[1] > 0


def test_set_final_position_all_zero():
    grid_field = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    final_position = (1, 1)
    grid_field_with_final_pos = GridEnvironment.set_final_positon(
        grid_field, final_position
    )
    expected_field = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 0]])

    assert np.array_equal(grid_field_with_final_pos, expected_field)


def test_set_final_position_asymmetric():
    grid_field = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
    final_position = (4, 3)
    grid_field_with_final_pos = GridEnvironment.set_final_positon(
        grid_field, final_position
    )
    expected_field = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 1], [0, 0, 0]])
    assert np.array_equal(grid_field_with_final_pos, expected_field)


def test_get_player_position():
    grid_shape = (3, 3)
    final_positon = (2, 1)
    player_position = GridEnvironment.get_player_position(grid_shape, final_positon)

    assert final_positon != player_position
    assert player_position[0] >= 1
    assert player_position[0] <= 3
    assert player_position[1] >= 1
    assert player_position[1] <= 3


def test_set_player_position():
    grid_field = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
    player_position = (4, 3)
    grid_field_with_player_pos = GridEnvironment.set_player_position(
        grid_field, player_position
    )
    expected_field = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 2], [0, 0, 0]])
    assert np.array_equal(grid_field_with_player_pos, expected_field)


def test_create_environment():
    env = GridEnvironment()
    grid_field = env.create_env()

    assert np.count_nonzero(grid_field == 2) == 1
    assert np.count_nonzero(grid_field == 1) == 1
