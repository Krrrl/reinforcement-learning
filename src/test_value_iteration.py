from env.gridworld import Gridworld
from policy_iteration import Gridworld_Agent

#env = Gridworld()
#env = Gridworld(5, 5, (4,0), {(0,3):1, (0,4):-1, (0,0):1}, [(1,1), (1,2)], [(0,3), (0,4), (0,0)])
env = Gridworld(10, 10, (5,5), {(0,0):1, (9,0):1, (0,9):1, (9,9):1, (0,4):-1, (4,0):-1, (4,9):-1, (9,4):-1}, [(1,1), (8,8), (1,8), (8,1)], [(0,0), (9,0), (0,9), (9,9), (0,4), (4,0), (4,9), (9,4)])
agent = Gridworld_Agent()

#VF = agent.value_iteration(env)

#agent.print_value_function(env)
#agent.set_policy_deterministic_greedy(env)
#agent.print_policy(env, agent.policy)

VF = agent.policy_iteration(env)