import numpy as np
import random


class Gridworld_Agent:

	def __init__(self, 
					method = 'value_iteration', 
					learning_rate = 0.1, 
					discount_factor = 0.9):

		self.VF = {}
		self.Policy = {}
		self.learning_rate = learning_rate
		self.discount_factor = discount_factor


	def get_value_function(self):
		return self.VF



	def update_value_function(self, state, value):
		new_value = self.VF.get(state, 0) + self.learning_rate*(value - self.VF.get(state, 0))
		self.VF[state] = new_value

	def init_VF_zeros(self, dimensions):
		for i in range(dimensions[0]):
			for j in range(dimensions[1]):
				self.VF[(i,j)] = 0


	def value_iteration(self, env, delta_treshold):

		#Psudocode
		#set treshold
		#create 0-value function
		#Iterate trough all states
		#Update value function for each step
		#if change < treshold, break loop
		world_dim = env.get_world_dim()

		self.init_VF_zeros(world_dim)

		height = world_dim[0]
		width = world_dim[1]

		done = False

		while(not done):
			delta = 0
			new_value = 0

			for i in range(0, height):
				for j in range(0, width):

					possible_moves = env.get_possible_moves((i,j))

					for k in possible_moves:
						new_value += env.survey_world(k) + self.discount_factor * self.VF[k]
					
					self.update_value_function((i,j), new_value)
					
					temp = new_value - self.VF[(i,j)]
					if(delta < temp):
						delta = temp

			if(delta < delta_treshold):
				done = True
	
	@staticmethod
	def random_policy(env):
		current_state = env.agent_position
		possible_moves = env.possible_moves(current_state)

		choice = random.choice(possible_moves)

		return choice


	def print_value_function(self):
		max_dim = np.max(list(self.VF.keys()), axis = 0)
		
		height = max_dim[0] + 1
		width = max_dim[1] + 1
		grid = np.zeros(max_dim) 
		

		for i in range(height):
			for j in range(width):
				grid[i][j] = self.VF.get((i,j), 0)

		print(grid)

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

		else:
			print('Illegal state change!')

		return tuple(new_state) 

	@staticmethod
	def cart2udlf(state, next_state):
		if(state[0] - new_state[0] == 1):
			command = 'U'
		elif(state[0] - new_state[0] == -1):
			command = 'D'
		elif(state[1] - new_state[1] == 1):
			command = 'L'
		elif(state[1] - new_state[1] == -1):
			command = 'R'

		return command


if __name__ == '__main__':
	print("We live in a binary reality")	