from src.overarching.config_schemas import EnvironmentConfig, AgentConfig

BASE_ENV_CONFIG = EnvironmentConfig(width=5, height=5)

BASE_AGENT_CONFIG = AgentConfig(
    learning_rate=0.1, decay=0.1, exploration_rate=0.1, discount_factor=0.1
)
