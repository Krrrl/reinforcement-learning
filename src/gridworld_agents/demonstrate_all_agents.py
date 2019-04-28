from gridworld_agents.monte_carlo_agent import Monte_Carlo_Agent
from env.gridworld import Gridworld

class Demonstrate_All_Agents(Monte_Carlo_Agent):
	pass

if __name__ == '__main__':
	print("This agent is made for the Gridworld environment. It has multiple methods implemented, namely: Value Iteration, Policy Iteration and Monte Carlo Approximation.")
	print("These methods can be demonstrated seperately from their respectively named demo files.")
	print("The following is the demo of all the above mentioned methods, running on the standard stochastic Gridworld-problem.")
	
	print("Value Iteration:")
	env = Gridworld(deterministic = False)
	agent = Demonstrate_All_Agents()
	agent.value_iteration(env)

	print("Policy Iteration:")
	env = Gridworld(deterministic = False)
	agent = Demonstrate_All_Agents()
	agent.policy_iteration(env)

	print("Monte-Carlo Approximation:")
	env = Gridworld(deterministic = False)
	agent = Demonstrate_All_Agents()
	agent.monte_carlo_approximation(1, env)
	#env = Gridworld(5, 5, (4,0), {(0,3):1, (0,4):-1, (0,0):1}, [(1,1), (1,2)], [(0,3), (0,4), (0,0)])
	#env = Gridworld(10, 10, (5,5), {(0,0):1, (9,0):1, (0,9):1, (9,9):1, (0,4):-1, (4,0):-1, (4,9):-1, (9,4):-1}, [(1,1), (8,8), (1,8), (8,1)], [(0,0), (9,0), (0,9), (9,9), (0,4), (4,0), (4,9), (9,4)])
	#VF = agent.value_iteration(env)

	#agent.print_value_function(env)
	#agent.set_policy_deterministic_greedy(env)
	#agent.print_policy(env, agent.policy)