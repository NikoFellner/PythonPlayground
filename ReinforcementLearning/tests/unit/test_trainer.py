from unittest.mock import Mock

from src.agents.q_agent import QAgent
from src.environment.grid_environment import GridEnvironment
from src.overarching.schemas import State, Action, GridAction, Reward, Goal
from src.trainer.trainer import Trainer


def test_trainer_run_episode():
    env = Mock(spec=GridEnvironment)
    agent = Mock(spec=QAgent)

    start_state = State(
        row_pos=0,
        column_pos=0,
    )

    next_state = State(
        row_pos=0,
        column_pos=1,
    )

    action = Action(
        action=GridAction.right,
    )

    reward = Reward(
        reward=1.0,
    )

    goal = Goal(reached=True)

    env.reset.return_value = start_state

    env.get_available_actions.return_value = [action]

    agent.select_action.return_value = action

    env.step.return_value = (next_state, reward, goal)

    trainer = Trainer(
        env=env,
        agent=agent,
    )

    result_reward = trainer.run_episode()

    agent.select_action.assert_called_once()
    agent.update.assert_called_once()
    env.get_available_actions.assert_called_once()
    env.step.assert_called_once()

    assert result_reward == 1


def test_train_returns_rewards():
    trainer = Trainer(
        env=Mock(),
        agent=Mock(),
    )

    trainer.run_episode = Mock(side_effect=[1.0, 2.0, 3.0])

    result = trainer.train(3)

    assert result == [1.0, 2.0, 3.0]


def test_train_calls_run_episode_n_times():
    trainer = Trainer(
        env=Mock(),
        agent=Mock(),
    )

    trainer.run_episode = Mock(return_value=1.0)

    trainer.train(5)

    assert trainer.run_episode.call_count == 5
