from abc import abstractmethod, ABC

from src.environment.schemas import State, Reward, Action


class Agent(ABC):
    @abstractmethod
    def select_action(self, state: State) -> Action:
        raise NotImplementedError

    @abstractmethod
    def update(
        self, state: State, action: Action, reward: Reward, next_state: State
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_q_value(self, state: State, action: Action) -> None:
        raise NotImplementedError

    @abstractmethod
    def set_q_value(self, state: State, action: Action, value: float) -> None:
        raise NotImplementedError
