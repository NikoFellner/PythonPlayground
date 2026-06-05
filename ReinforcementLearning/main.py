from src.environment.grid_environment import GridEnvironment

env = GridEnvironment()
grid = env.create_env()

env.print_grid(grid)
