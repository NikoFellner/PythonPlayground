import random
from collections import defaultdict

from src.agents.agent import Agent
from src.overarching.config_schemas import AgentConfig
from src.overarching.schemas import State, Action, GridAction, Reward

GRID_ACTIONS = [
    Action(action=GridAction.up),
    Action(action=GridAction.down),
    Action(action=GridAction.left),
    Action(action=GridAction.right),
]


class QAgent(Agent):
    def __init__(self, config: AgentConfig):
        self._learning_rate = config.learning_rate
        self._discount_factor = config.discount_factor
        self._exploration_rate = config.exploration_rate
        self._decay = config.decay

        self._q_table: defaultdict = defaultdict(
            lambda: defaultdict(lambda: defaultdict(float))
        )

    def select_action(self, state: State, available_actions: list[Action]) -> Action:
        if random.random() < self._exploration_rate:
            return random.choice(available_actions)
        else:
            max_q = max(self.get_q_value(state, action) for action in available_actions)

            best_actions = [
                action
                for action in available_actions
                if self.get_q_value(state, action) == max_q
            ]

            return random.choice(best_actions)

    def update(
        self, state: State, action: Action, reward: Reward, next_state: State
    ) -> None:
        current_q_value = self.get_q_value(state, action)
        next_q_vals = self.get_all_q_values_from_state(next_state)
        max_next_q_val = max(next_q_vals)
        new_q_val = self.calculate_q_val(current_q_value, max_next_q_val, reward)
        self.set_q_value(state, action, new_q_val)

    def calculate_q_val(self, q_current: float, q_next: float, reward: Reward) -> float:
        return q_current + self._learning_rate * (
            reward.reward + self._discount_factor * q_next - q_current
        )

    def get_all_q_values_from_state(self, state: State) -> list[float]:
        q_vals: list[float] = []
        for grid_action in GRID_ACTIONS:
            q_vals.append(self.get_q_value(state, grid_action))
        return q_vals

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
