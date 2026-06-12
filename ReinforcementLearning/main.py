from src.overarching.config_schemas import AgentConfig, EnvironmentConfig

agent_config = AgentConfig(
    learning_rate=0.1, exploration_rate=0.1, decay=0.1, discount_factor=0.1
)

env_config = EnvironmentConfig(width=5, height=5)
