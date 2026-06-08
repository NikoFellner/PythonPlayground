from abc import abstractmethod, ABC

from src.environment.schemas import Action, State, Reward, Goal


class Environment(ABC):
    @abstractmethod
    def step(self, action: Action) -> tuple[State, Reward, Goal]:
        raise NotImplementedError

    @abstractmethod
    def get_available_actions(self) -> list[Action]:
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError
