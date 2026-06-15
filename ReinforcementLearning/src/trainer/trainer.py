from loguru import logger
from src.agents.agent import Agent
from src.environment.grid_environment import GridEnvironment


class Trainer:
    def __init__(self,*, env: GridEnvironment, agent: Agent):
        self._env = env
        self._agent = agent

    def run_episode(self) -> float:
        episode_finished: bool = False
        overall_reward: float = 0
        logger.info("Episode started")
        while not episode_finished:
            logger.info("Get Actions")
            available_actions = self._env.get_available_actions()
            player_state = self._env.player_state
            logger.info(f"Player position {player_state}")
            logger.info(f"choose action from {available_actions}")
            selected_action = self._agent.select_action(player_state, available_actions)
            logger.info("Do one step")
            next_state, reward, goal = self._env.step(selected_action)
            overall_reward += reward.reward
            logger.info("update q values")
            self._agent.update(player_state, selected_action, reward, next_state)
            episode_finished = goal.reached
        return overall_reward

    def train(self, num_episodes: int) -> list[float]:
        rewards_of_all_episodes: list[float] = []
        logger.info(f"Starting training with {num_episodes}")
        for episode in range(num_episodes):
            logger.info(f"Episode: {episode}/{num_episodes}")
            rewards_of_all_episodes.append(self.run_episode())
            self._env.reset()
        return rewards_of_all_episodes
