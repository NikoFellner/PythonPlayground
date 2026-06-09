
from src.agents.QAgent import QAgent
from src.environment.schemas import State, Action, GridAction


def test_get_q_value_given_value():
    qagent = QAgent()
    qagent._q_table[2][2][GridAction.up] = 0.4
    q_value = qagent.get_q_value(
        State(row_pos=2, column_pos=2), Action(action=GridAction.up)
    )
    assert q_value == 0.4


def test_get_q_value_no_value():
    qagent = QAgent()

    q_value = qagent.get_q_value(
        State(row_pos=2, column_pos=2), Action(action=GridAction.down)
    )
    assert q_value == 0.0


def test_set_q_agent_value():
    qagent = QAgent()
    state = State(row_pos=2, column_pos=2)
    action = Action(action=GridAction.down)
    q_value = 0.5
    initial_value = qagent.get_q_value(state, action)
    qagent.set_q_value(state, action, q_value)
    new_value = qagent.get_q_value(state, action)
    assert initial_value == 0.0
    assert new_value == 0.5


def test_set_q_agent_value_updated():
    qagent = QAgent()
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
    qagent = QAgent()
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
