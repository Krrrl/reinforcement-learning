from env.gridworld import Gridworld
from policy_iteration import Gridworld_Agent

env = Gridworld()
agent = Gridworld_Agent()

agent.value_iteration(env, 0.02)
agent.print_value_function()
