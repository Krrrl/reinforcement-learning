import numpy as np
import random as rn

#all positions are given as a (h,w) tupple.

class Gridworld:


	def __init__(self, 
					height_width = (3, 4), 
					agent_start_pos = (2, 0), 
					rewards = {(0,3):1, (1,3):-1}, 
					walls = [(1,1)],
					terminals = [(0,3), (1,3)], 
					action_penalty = 0,
					deterministic = True,
					randomness_probability = 0.5
				):

		self.gridworld = np.zeros(height_width)
		self.agent_position = agent_start_pos
		self.agent_prev_position = agent_start_pos
		self.reward_positions = rewards
		self.wall_positions = walls
		self.terminal_positions = terminals
		self.action_penalty = action_penalty
		self.game_over = False
		
		self.deterministic = deterministic
		self.randomness_probability = randomness_probability


	def action_randomizer(self, state, intended_next_state):

		if(rn.random() > self.randomness_probability):
			return intended_next_state
		
		possible_next_states = self.get_possible_next_states(state)
		possible_next_states.remove(intended_next_state)
		random_moves = possible_next_states
		
		return rn.choice(random_moves)

	def get_action_probabilities(self, state, intended_next_state, possible_next_states):
		
		if(state in self.terminal_positions):
			probabilities = {intended_next_state : 0}
			return probabilities 

		if(self.deterministic):
			probabilities = {intended_next_state : 1}
			return probabilities

		probabilities = {}

		probabilities[intended_next_state] = 1 - self.randomness_probability
		possible_next_states.remove(intended_next_state)

		for state in possible_next_states:
			probabilities[state] = self.randomness_probability/len(possible_next_states)

		return probabilities


	def set_reward_state(self, position, reward):
		self.reward_positions[position] = reward
		self.gridworld[position[0]][position[1]] = reward

	def set_wall_state(self, position):
		self.wall_positions.append(position)
		self.gridworld[position[0]][position[1]] = None

	def set_terminal_state(self, position):
		self.terminal_positions.append(position)

	def set_agent_position(self, position):
		self.agent_position = position

	def get_all_parameters(self):
		parameters = {}

		parameters["height_width"] = self.get_world_dim()
		parameters["agent_position"] = self.agent_position
		parameters["reward_positions"] = self.reward_positions
		parameters["wall_positions"] = self.wall_positions
		parameters["terminal_positions"] = self.terminal_positions
		parameters["action_penalty"] = self.action_penalty
		parameters["deterministic"] = self.deterministic
		parameters["randomness_probability"] = self.randomness_probability

		return parameters


	def get_agent_position(self):
		return self.agent_position

	def get_world_dim(self):
		return np.shape(self.gridworld)

	def get_all_non_wall_states(self):
		all_possible_states = []
		
		world_dimension = self.get_world_dim()
		world_height = world_dimension[0]
		world_width = world_dimension[1]

		for i in range(world_height):
			for j in range(world_width):
				if((i,j) not in self.wall_positions):
					all_possible_states.append((i,j))

		return all_possible_states

	def get_possible_next_states(self, position):
		possible_next_states = []

		if((position in self.terminal_positions) or (position in self.wall_positions)):
			possible_next_states.append(position)
			return possible_next_states

		gridworld_dimension = np.shape(self.gridworld)
		gridworld_height = gridworld_dimension[0]
		gridworld_width = gridworld_dimension[1]

		position_height = position[0]
		position_width = position[1]

		if(((position_height + 1) in range(gridworld_height)) and ((position_height + 1, position_width) not in self.wall_positions)):
				move = (position_height + 1, position_width)
				possible_next_states.append(move)

		if(((position_height - 1) in range(gridworld_height)) and ((position_height - 1, position_width) not in self.wall_positions)):
				move = (position_height - 1, position_width)
				possible_next_states.append(move)

		if(((position_width + 1) in range(gridworld_width)) and ((position_height, position_width + 1) not in self.wall_positions)):
				move = (position_height, position_width + 1)
				possible_next_states.append(move)
				#possible_next_states = np.append(possible_next_states, self.gridworld[position[0]][position[1] + 1])
		
		if(((position_width - 1) in range(gridworld_width)) and ((position_height, position_width - 1) not in self.wall_positions)):
				move = (position_height, position_width - 1)
				possible_next_states.append(move)
				
				#possible_next_states = np.append(possible_next_states, self.gridworld[position[0]][position[1] - 1])
			

		return possible_next_states

	def survey_world(self, position, next_position):
		return self.reward_positions.get(next_position, self.action_penalty)

	def agent_move(self, new_agent_position):
		if(self.game_over):
			print("Illegal move, the game is over already! \n")
			return None
		if(self.agent_position == new_agent_position):
			return self.agent_position, self.action_penalty

		if(new_agent_position in self.get_possible_next_states(self.agent_position)):
			
			if(not self.deterministic):
				new_agent_position = self.action_randomizer(self.agent_position, new_agent_position)

			self.agent_prev_position = self.agent_position
			self.agent_position = new_agent_position

			if(self.check_game_over()):
				self.game_over = True

			if(self.agent_position in self.reward_positions):
				return self.agent_position, self.reward_positions[self.agent_position]
			else:
				return self.agent_position, self.action_penalty
		else:
			print('Illegal move.')
			return None
	
	def undo_last_move(self):
		self.agent_position = self.agent_prev_position
		if(self.game_over):
			self.game_over = False


	def is_terminal(self, position):
		if(position in self.terminal_positions):
			return True
		else:
			return False

	def check_game_over(self):
		if(self.is_terminal(self.agent_position)):
			return True
		else:
			return False


	def print_gridworld(self):
		temp = self.gridworld
		temp[self.agent_prev_position] = 0
		temp[self.agent_position] = 100
		print(self.gridworld)
		print("\n Agent position: {} \n".format(self.agent_position))


if __name__ == '__main__':
	print("Creating Gridworld object: with 3x4 dimensions and agent start in (2, 0), with a wall in (1,1)\n")
	x = Gridworld()
	x.set_wall_state((1,1))
	print("Also added is a terminal state in (0,3), with a reward of 1, and in (1,3) a reward of -1 \n")
	x.set_reward_state((0,3), 1)
	x.set_reward_state((1,3), -1)
	x.print_gridworld()

	agent_possible_moves = x.get_possible_next_states(x.agent_position)
	print("Here are the agents possible moves from state {} : {} \n".format(x.agent_position, agent_possible_moves))
	next_agent_pos = rn.choice(agent_possible_moves)
	print("Agent then moves to {} \n".format(next_agent_pos))
	x.agent_move(next_agent_pos)
	x.print_gridworld()
	agent_possible_moves = x.get_possible_next_states(x.agent_position)
	print("Here are the agents possible moves from state {} : {} \n".format(x.agent_position, agent_possible_moves))

