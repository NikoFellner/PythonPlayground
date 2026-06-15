from src.agents.q_agent import QAgent
from src.environment.grid_environment import GridEnvironment
from src.overarching.config_schemas import AgentConfig, EnvironmentConfig
from src.overarching.result_plotter import ResultPlotter
from src.trainer.trainer import Trainer
import seaborn as sns

agent_config = AgentConfig(
    learning_rate=0.1, exploration_rate=0.9, decay=0.95, discount_factor=0.95
)

env_config = EnvironmentConfig(width=5, height=5)

env = GridEnvironment(env_config)
agent = QAgent(agent_config)

trainer = Trainer(env=env, agent=agent)

results = trainer.train(1000)

ResultPlotter.plot_rewards(results)

print(results)
