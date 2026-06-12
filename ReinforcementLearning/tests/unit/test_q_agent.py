from src.agents.QAgent import QAgent
from src.environment.grid_environment import GridEnvironment
from src.environment.schemas import State, Action, GridAction


def test_get_q_value_given_value():
    env = GridEnvironment()
    qagent = QAgent(env)
    qagent._q_table[2][2][GridAction.up] = 0.4
    q_value = qagent.get_q_value(
        State(row_pos=2, column_pos=2), Action(action=GridAction.up)
    )
    assert q_value == 0.4


def test_get_q_value_no_value():
    env = GridEnvironment()
    qagent = QAgent(env)

    q_value = qagent.get_q_value(
        State(row_pos=2, column_pos=2), Action(action=GridAction.down)
    )
    assert q_value == 0.0


def test_set_q_agent_value():
    env = GridEnvironment()
    qagent = QAgent(env)
    state = State(row_pos=2, column_pos=2)
    action = Action(action=GridAction.down)
    q_value = 0.5
    initial_value = qagent.get_q_value(state, action)
    qagent.set_q_value(state, action, q_value)
    new_value = qagent.get_q_value(state, action)
    assert initial_value == 0.0
    assert new_value == 0.5


def test_set_q_agent_value_updated():
    env = GridEnvironment()
    qagent = QAgent(env)
    state = State(row_pos=2, column_pos=2)
    action = Action(action=GridAction.down)
    q_value_1 = 0.5
    q_value_2 = 0.9
    qagent.set_q_value(state, action, q_value_1)
    result_value_1 = qagent.get_q_value(state, action)
    qagent.set_q_value(state, action, q_value_2)
    result_value_2 = qagent.get_q_value(state, action)
    assert result_value_1 == 0.5
    assert result_value_2 == 0.9


def test_set_q_agent_for_different_action():
    env = GridEnvironment()
    qagent = QAgent(env)
    state = State(row_pos=2, column_pos=2)
    action_1 = Action(action=GridAction.down)
    action_2 = Action(action=GridAction.up)
    q_value_1 = 0.5
    q_value_2 = 0.9
    qagent.set_q_value(state, action_1, q_value_1)
    qagent.set_q_value(state, action_2, q_value_2)
    result_value_1 = qagent.get_q_value(state, action_1)
    result_value_2 = qagent.get_q_value(state, action_2)
    assert result_value_1 == 0.5
    assert result_value_2 == 0.9


def test_select_action_max_q():
    env = GridEnvironment()

    qagent = QAgent(env, exploration_rate=0)
    state = State(row_pos=2, column_pos=2)

    env._player_position = state
    action_1 = Action(action=GridAction.down)
    action_2 = Action(action=GridAction.up)
    q_value_1 = 0.5
    q_value_2 = 0.9
    qagent.set_q_value(state, action_1, q_value_1)
    qagent.set_q_value(state, action_2, q_value_2)
    selected_action = qagent.select_action(state)
    assert selected_action == action_2


def test_select_action_same_max_q():
    env = GridEnvironment()
    qagent = QAgent(env, exploration_rate=0)
    state = State(row_pos=2, column_pos=2)
    env._player_position = state
    action_1 = Action(action=GridAction.down)
    action_2 = Action(action=GridAction.right)
    action_3 = Action(action=GridAction.left)
    # since up ist the first value in GRID_ACTIONS it will choose
    action_4 = Action(action=GridAction.up)
    q_value_1 = 0.9
    q_value_2 = 0.9
    q_value_3 = 0.9
    q_value_4 = 0.9
    qagent.set_q_value(state, action_1, q_value_1)
    qagent.set_q_value(state, action_2, q_value_2)
    qagent.set_q_value(state, action_3, q_value_3)
    qagent.set_q_value(state, action_4, q_value_4)
    selected_action = qagent.select_action(state)
    assert selected_action == action_1 or action_2 or action_3 or action_4


def test_select_action_same_max_q_only_available_action():
    env = GridEnvironment()
    qagent = QAgent(env, exploration_rate=0)
    state = State(row_pos=1, column_pos=1)
    env._player_position = state
    # only availbale selections are right or down
    action_1 = Action(action=GridAction.down)
    action_2 = Action(action=GridAction.right)
    action_3 = Action(action=GridAction.left)
    action_4 = Action(action=GridAction.up)
    q_value_1 = 0.9
    q_value_2 = 0.9
    q_value_3 = 0.9
    q_value_4 = 0.9
    qagent.set_q_value(state, action_1, q_value_1)
    qagent.set_q_value(state, action_2, q_value_2)
    qagent.set_q_value(state, action_3, q_value_3)
    qagent.set_q_value(state, action_4, q_value_4)
    selected_action = qagent.select_action(state)
    assert selected_action == action_1 or action_1
