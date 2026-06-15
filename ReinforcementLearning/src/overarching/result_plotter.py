import seaborn as sns
import matplotlib.pyplot as plt

class ResultPlotter:
    @staticmethod
    def plot_rewards(rewards:list[float]):
        sns.lineplot(
            x=range(len(rewards)),
            y=rewards,
        )

        plt.xlabel("Episode")
        plt.ylabel("Reward")
        plt.title("Reward per Episode")
        plt.show()