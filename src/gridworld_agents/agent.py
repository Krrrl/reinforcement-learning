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
	print("The Gridworld_Agent class contains the base framework all agents needs to interact with the Gridworld environment.")
	print("All other gridworld agents are children/inherets from this class.")
	print("Gridworld_Agent itself contains no methods for solving the Gridworld Problem.")
