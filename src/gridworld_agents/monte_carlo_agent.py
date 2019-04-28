import numpy as np
import random

from gridworld_agents.policy_iteration_agent import Policy_Iteration_Agent
from env.gridworld import Gridworld
from custom_lib.magic_hat import update_sample_mean

class Monte_Carlo_Agent(Policy_Iteration_Agent):

	def __init__(self, 
					learning_rate = 0.1, 
					discount_factor = 0.9,
					delta_treshold = 0.002):

		self.VF = {}
		self.policy = {}
		self.learning_rate = learning_rate
		self.discount_factor = discount_factor
		self.delta_treshold = delta_treshold

	def play_game(self, env, policy):

		list_of_states = []
		list_of_rewards = []
		list_of_states.append(env.get_agent_position())
		list_of_rewards.append(0)

		while(not env.game_over):
			new_state, reward = env.agent_move(policy[env.get_agent_position()])
			list_of_states.append(new_state)
			list_of_rewards.append(reward)
			
		return list_of_states, list_of_rewards

	def monte_carlo_approximation(self, number_of_episodes, env = None):

		if(env):
			parameters = env.get_all_parameters()

		else:
			env = Gridworld()
			parameters = None

		policy = self.set_policy_random(env)
		self.print_policy(env, policy)
		#VF_value_iterated, policy = self.policy_iteration(env)

		for i in range(number_of_episodes):

			if parameters:
				env = Gridworld(parameters["height_width"], 
								parameters["agent_position"],
								parameters["reward_positions"],
								parameters["wall_positions"],
								parameters["terminal_positions"],
								parameters["action_penalty"],
								parameters["deterministic"],
								parameters["randomness_probability"])
			else:
				env = Gridworld()


			list_of_states, list_of_rewards = self.play_game(env, policy)	
			print("Result of the episode: ")
			print(list_of_states)
			print(list_of_rewards)

			CALCULATE AVERAGE RETURNS
			update_sample_mean(10,10,10)

			del env


if __name__ == '__main__':
	print("This agent is made for the Gridworld environment, using the Monte Carlo Method to estimate the value function.")
	print("The following is the demo of the Monte Carlo Approximation Method for solving the prediction problem, running on the standard stochastic Gridworld environment.")
	
	print("Monte-Carlo Approximation:")
	env = Gridworld(deterministic = False, randomness_probability = 0.33)
	agent = Monte_Carlo_Agent()
	agent.monte_carlo_approximation(1, env)
	#env = Gridworld(5, 5, (4,0), {(0,3):1, (0,4):-1, (0,0):1}, [(1,1), (1,2)], [(0,3), (0,4), (0,0)])
	#env = Gridworld(10, 10, (5,5), {(0,0):1, (9,0):1, (0,9):1, (9,9):1, (0,4):-1, (4,0):-1, (4,9):-1, (9,4):-1}, [(1,1), (8,8), (1,8), (8,1)], [(0,0), (9,0), (0,9), (9,9), (0,4), (4,0), (4,9), (9,4)])
	#VF = agent.value_iteration(env)

	#agent.print_value_function(env)
	#agent.set_policy_deterministic_greedy(env)
	#agent.print_policy(env, agent.policy)