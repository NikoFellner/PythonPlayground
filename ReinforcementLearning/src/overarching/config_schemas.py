from pydantic import BaseModel


class AgentConfig(BaseModel):
    learning_rate: float
    exploration_rate: float
    discount_factor: float
    decay: float


class EnvironmentConfig(BaseModel):
    width: int
    height: int
