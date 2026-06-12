from src.agents.q_agent import QAgent
from src.environment.grid_environment import GridEnvironment
from src.overarching.config_schemas import AgentConfig, EnvironmentConfig
from src.overarching.configs import BASE_AGENT_CONFIG, BASE_ENV_CONFIG


class DependencyInjection:
    def __init__(
        self,
        agent_config: AgentConfig,
        environment_config: EnvironmentConfig,
    ):
        self._agent_config: AgentConfig = agent_config
        self._environment_config: EnvironmentConfig = environment_config

    @property
    def agent(self):
        return QAgent(self._agent_config)

    @property
    def env(self):
        return GridEnvironment(self._environment_config)


DI = DependencyInjection(
    agent_config=BASE_AGENT_CONFIG, environment_config=BASE_ENV_CONFIG
)
