import numpy as np
import random

from gridworld_agents.value_iteration_agent import Value_Iteration_Agent
from env.gridworld import Gridworld
from custom_lib.magic_hat import update_sample_mean

class Policy_Iteration_Agent(Value_Iteration_Agent):

	def __init__(self, 
					learning_rate = 0.1, 
					discount_factor = 0.9,
					delta_treshold = 0.002):

		self.VF = {}
		self.policy = {}
		self.learning_rate = learning_rate
		self.discount_factor = discount_factor
		self.delta_treshold = delta_treshold

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

if __name__ == '__main__':
	print("This agent is made for the Gridworld environment. It uses Value Iteration for its Policy Improvement step.")
	print("The following is a demo of the Policy Iteration algorithm, solving the control problem on the standard stochastic Gridworld.")

	print("Policy Iteration:")
	env = Gridworld(deterministic = False)
	agent = Policy_Iteration_Agent()
	agent.policy_iteration(env)

	#env = Gridworld(5, 5, (4,0), {(0,3):1, (0,4):-1, (0,0):1}, [(1,1), (1,2)], [(0,3), (0,4), (0,0)])
	#env = Gridworld(10, 10, (5,5), {(0,0):1, (9,0):1, (0,9):1, (9,9):1, (0,4):-1, (4,0):-1, (4,9):-1, (9,4):-1}, [(1,1), (8,8), (1,8), (8,1)], [(0,0), (9,0), (0,9), (9,9), (0,4), (4,0), (4,9), (9,4)])
	#VF = agent.value_iteration(env)

	#agent.print_value_function(env)
	#agent.set_policy_deterministic_greedy(env)
	#agent.print_policy(env, agent.policy)