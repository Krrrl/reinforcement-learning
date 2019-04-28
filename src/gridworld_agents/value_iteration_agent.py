import numpy as np
import random

from gridworld_agents.agent import Gridworld_Agent
from env.gridworld import Gridworld
from custom_lib.magic_hat import update_sample_mean

class Value_Iteration_Agent(Gridworld_Agent):

	def __init__(self, 
					learning_rate = 0.1, 
					discount_factor = 0.9,
					delta_treshold = 0.002):

		self.VF = {}
		self.policy = {}
		self.learning_rate = learning_rate
		self.discount_factor = discount_factor
		self.delta_treshold = delta_treshold

	def init_VF_zeros(self, env):
		all_states = env.get_all_non_wall_states()

		for state in all_states:
			self.VF[state] = 0

	def update_value_function(self, state, value):
		new_value = self.VF.get(state, 0) + self.learning_rate*(value - self.VF.get(state, 0))
		self.VF[state] = new_value

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

if __name__ == '__main__':
	print("This agent is made for the Gridworld environment. It uses Value Iteration to create a value function for the environment.")
	print("The following is a demo of the Value Iteration algorithm solving the prediction problem on the standard stochastic Gridworld-problem.")
	
	print("Value Iteration:")
	env = Gridworld(deterministic = False)
	agent = Value_Iteration_Agent()
	agent.value_iteration(env)