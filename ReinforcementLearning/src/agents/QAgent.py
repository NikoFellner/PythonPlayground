from collections import defaultdict

from src.agents.agent import Agent
from src.environment.schemas import State, Action, GridAction, Reward


class QAgent(Agent):
    def __init__(
        self,
        learning_rate: float = 0.01,
        discount_factor: float = 0.95,
        exploration_rate: float = 0.01,
        decay: float = 0.01,
    ):
        self._learning_rate = learning_rate
        self._discount_factor = discount_factor
        self._exploration_rate = exploration_rate
        self._decay = decay

        self._q_table: defaultdict = defaultdict(
            lambda: defaultdict(lambda: defaultdict(float))
        )

    def select_action(self, state: State) -> Action:
        return Action(action=GridAction.up)

    def update(
        self, state: State, action: Action, reward: Reward, next_state: State
    ) -> None:
        raise NotImplementedError

    def get_q_value(self, state: State, action: Action) -> float:
        row_value = state.row_pos
        col_value = state.column_pos
        action_value = action.action
        return self._q_table[row_value][col_value][action_value]

    def set_q_value(self, state: State, action: Action, q_value: float) -> None:
        row_value = state.row_pos
        column_value = state.column_pos
        action_value = action.action
        self._q_table[row_value][column_value][action_value] = q_value
