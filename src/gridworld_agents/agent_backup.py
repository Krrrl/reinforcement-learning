import numpy as np
import random

from env.gridworld import Gridworld
from custom_lib.magic_hat import update_sample_mean

class Gridworld_Agent:

	def __init__(self, 
					learning_rate = 0.1, 
					discount_factor = 0.9,
					delta_treshold = 0.002):

		self.VF = {}
		self.policy = {}
		self.learning_rate = learning_rate
		self.discount_factor = discount_factor
		self.delta_treshold = delta_treshold


	def get_value_function(self):
		return self.VF

	def get_policy(self):
		return self.policy

	def update_value_function(self, state, value):
		new_value = self.VF.get(state, 0) + self.learning_rate*(value - self.VF.get(state, 0))
		self.VF[state] = new_value

	def init_VF_zeros(self, env):
		all_states = env.get_all_non_wall_states()

		for state in all_states:
			self.VF[state] = 0

	def value_iteration(self, env):
		all_states = env.get_all_non_wall_states()

		self.init_VF_zeros(env)


		while(True):

			highest_delta = 0

			for state in all_states:
				
				possible_next_states = env.get_possible_next_states(state)
				
				best_next_state_value = 0
				

				for intended_next_state in possible_next_states:
					state_transition_probabilities = env.get_action_probabilities(state, intended_next_state, possible_next_states)
					intended_next_state_value = 0

					for resulting_next_state in state_transition_probabilities:
						intended_next_state_value += state_transition_probabilities[resulting_next_state]*(env.survey_world(state, resulting_next_state) + self.discount_factor * self.VF[resulting_next_state])
					
					if(best_next_state_value <= intended_next_state_value):
						best_next_state_value = intended_next_state_value

				if(highest_delta < abs(best_next_state_value - self.VF[state])):
					highest_delta = abs(best_next_state_value - self.VF[state])

				self.update_value_function(state, best_next_state_value)

			if(highest_delta < self.delta_treshold):
				break

		self.print_value_function(env)

		return self.VF


	def policy_iteration(self, env):
		
		self.init_VF_zeros(env)

		policy = self.set_policy_random(env)

		previous_policy = {}

		while(policy != previous_policy):
			previous_VF = self.VF
			previous_policy = policy

			#new_VF = self.value_iteration(env, policy)
			new_VF = self.value_iteration(env)
			policy = self.set_policy_deterministic_greedy(env)



		self.print_value_function(env)
		self.print_policy(env, policy)
		
		return self.VF, policy

		#1.init VF and policy randomly
		#2.Do value iteration
		#3.policy impovement, if no change in policy it is done
		#4.policy evaluation(do VI again)
		#5.

	def get_greedy_next_state(self, env, state):
		states = []
		state_values = []
		#best_next_state = []

		possible_next_states = env.get_possible_next_states(state)

		if([state] == possible_next_states):
			return state

		for next_state in possible_next_states:
			state_values.append(env.survey_world(state, next_state) + self.VF[next_state])
			states.append(next_state)

		largest_value_index = np.argmax(state_values)
		chosen_state = states[largest_value_index]


		#largest_value = max(state_values)
		
		#if(state_values.count(largest_value) > 1):
		#	for i in range(len(states)):
		#		if(state_values[i] == largest_value):
		#			best_next_state.append(states[i])

		#else:
		#	best_next_state.append(states[np.argmax(state_values)])

		#chosen_state = random.choice(best_next_state)		
		
		return chosen_state			

	def set_policy_deterministic_greedy(self, env):
		all_states = env.get_all_non_wall_states()
		policy = {}

		for state in all_states:
			policy[state] = self.get_greedy_next_state(env, state)
		
		self.policy = policy

		return policy


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

		VF_value_iterated, policy = self.policy_iteration(env)
		print("This is the policy from the policy iteration")
		print(policy)

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

			update_sample_mean(10,10,10)

			del env
			


	@staticmethod
	def get_random_next_state(env, state):
		possible_moves = env.get_possible_next_states(state)

		choice = random.choice(possible_moves)

		return choice

	def set_policy_random(self, env):
		all_states = env.get_all_non_wall_states()
		policy = {}

		for state in all_states:
			policy[state] = self.get_random_next_state(env, state)

		self.policy = policy

		return policy

	@staticmethod
	def udlf2cart(state, command):
		new_state = list(state)

		if(command == 'U'):
			new_state[0] -= 1

		elif(command == 'D'):
			new_state[0] += 1

		elif(command == 'L'):
			new_state[1] -= 1

		elif(command == 'R'):
			new_state[1] += 1
		
		elif(command == 'S'):
			pass

		else:
			print('Illegal state change!')

		return tuple(new_state) 

	@staticmethod
	def cart2udlf(state, next_state):

		if(state[0] - next_state[0] == 1):
			command = 'U'
		elif(state[0] - next_state[0] == -1):
			command = 'D'
		elif(state[1] - next_state[1] == 1):
			command = 'L'
		elif(state[1] - next_state[1] == -1):
			command = 'R'
		elif(state == next_state):
			command = 'S'
		else:
			print("{} to {} is an illegal move!!".format(state, next_state))
			command = '?'

		return command

	def print_value_function(self, env):

		possible_states = env.get_all_non_wall_states()

		world_dim = env.get_world_dim()
		world_height = world_dim[0]
		world_width = world_dim[1]

		print("Printing Value Function: \n")
		
		for i in range(world_height):
			for j in range(world_width):
				print(" | {0:.2f} | ".format(self.VF.get((i,j), 0.0)), end = '')
			print("\n")					

	def print_policy(self, env, policy):
		printable_form = {}

		for state in policy:
			printable_form[state] = self.cart2udlf(state, policy[state])
		
		possible_states = env.get_all_non_wall_states()

		world_dim = env.get_world_dim()
		world_height = world_dim[0]
		world_width = world_dim[1]

		print("Printing Policy: \n")
		for i in range(world_height):
			for j in range(world_width):
				print(" | {} | ".format(printable_form.get((i,j), 0)), end = '')
			print("\n")


if __name__ == '__main__':
	print("This agent is made for the Gridworld environment. It has multiple methods implemented, namely: Value Iteration, Policy Iteration and Monte Carlo Approximation.")
	print("These methods can be demonstrated seperately from their respectively named demo files.")
	print("The following is the demo of all the above mentioned methods, running on the standard stochastic Gridworld-problem.")
	
	print("Value Iteration:")
	env = Gridworld(deterministic = False)
	agent = Gridworld_Agent()
	agent.value_iteration(env)

	print("Policy Iteration:")
	env = Gridworld(deterministic = False)
	agent = Gridworld_Agent()
	agent.policy_iteration(env)

	print("Monte-Carlo Approximation:")
	env = Gridworld(deterministic = False)
	agent = Gridworld_Agent()
	agent.monte_carlo_approximation(1, env)
	#env = Gridworld(5, 5, (4,0), {(0,3):1, (0,4):-1, (0,0):1}, [(1,1), (1,2)], [(0,3), (0,4), (0,0)])
	#env = Gridworld(10, 10, (5,5), {(0,0):1, (9,0):1, (0,9):1, (9,9):1, (0,4):-1, (4,0):-1, (4,9):-1, (9,4):-1}, [(1,1), (8,8), (1,8), (8,1)], [(0,0), (9,0), (0,9), (9,9), (0,4), (4,0), (4,9), (9,4)])
	#VF = agent.value_iteration(env)

	#agent.print_value_function(env)
	#agent.set_policy_deterministic_greedy(env)
	#agent.print_policy(env, agent.policy)