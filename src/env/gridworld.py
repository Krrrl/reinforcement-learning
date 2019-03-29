import numpy as np
import random as rn

#all positions are given as a (h,w) tupple.

class Gridworld:


	def __init__(self, 
					height = 3, 
					width = 4, 
					agent_start_pos = (2, 0), 
					rewards = {(0,3):1, (1,3):-1}, 
					walls = [(1,1)],
					terminals = [(0,3), (1,3)], 
					action_penalty = 0):

		self.gridworld = np.zeros((height, width))
		self.agent_position = agent_start_pos
		self.agent_prev_position = agent_start_pos
		self.reward_positions = rewards
		self.wall_positions = walls
		self.terminal_positions = terminals
		self.action_penalty = action_penalty
		self.game_over = False


	def set_reward_state(self, position, reward):
		self.reward_positions[position] = reward
		self.gridworld[position[0]][position[1]] = reward

	def set_wall_state(self, position):
		self.wall_positions.append(position)
		self.gridworld[position[0]][position[1]] = None

	def set_terminal_state(self, position):
		self.terminal_positions.append(position)

	def get_agent_pos(self):
		return self.agent_position

	def get_world_dim(self):
		return np.shape(self.gridworld)

	def get_possible_moves(self, position):
		poss_moves = []
		gridworld_dimension = np.shape(self.gridworld)

		if(((position[0] + 1) in range(gridworld_dimension[0])) and (not(np.isnan(self.gridworld[position[0] + 1][position[1]])))):
				move = (position[0] + 1, position[1])
				poss_moves.append(move)

		if(((position[0] - 1) in range(gridworld_dimension[0])) and (not(np.isnan(self.gridworld[position[0] - 1][position[1]])))):
				move = (position[0] - 1, position[1])
				poss_moves.append(move)

		if(((position[1] + 1) in range(gridworld_dimension[1])) and (not(np.isnan(self.gridworld[position[0]][position[1] + 1])))):
				move = (position[0], position[1] + 1)
				poss_moves.append(move)
				#poss_moves = np.append(poss_moves, self.gridworld[position[0]][position[1] + 1])
		
		if(((position[1] - 1) in range(gridworld_dimension[1])) and (not(np.isnan(self.gridworld[position[0]][position[1] - 1])))):
				move = (position[0], position[1] - 1)
				poss_moves.append(move)
				
				#poss_moves = np.append(poss_moves, self.gridworld[position[0]][position[1] - 1])
			

		return poss_moves

	def survey_world(self, position):
		if(position in self.reward_positions):
			return self.reward_positions[position]
		else:
			return self.action_penalty

	def agent_move(self, new_agent_position):
		if(self.game_over):
			print("Print, Illegal move, the game is over already! \n")
			return None
		if(new_agent_position in self.get_possible_moves(self.agent_position)):
			self.agent_prev_position = self.agent_position
			self.agent_position = new_agent_position

			if(game_over()):
				self.game_over = True

			if(self.agent_position in self.reward_positions):
				return reward_positions[self.agent_position]
			else:
				return self.action_penalty
		else:
			print('Illegal move.')
			return None
	
	def undo_last_move(self):
		self.agent_position = self.agent_prev_position


	def is_terminal(self, position):
		if(position in self.terminal_positions):
			return True
		else:
			return False

	def game_over(self):
		if(is_terminal(self.agent_position)):
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

	agent_possible_moves = x.get_possible_moves(x.agent_position)
	print("Here are the agents possible moves from state {} : {} \n".format(x.agent_position, agent_possible_moves))
	next_agent_pos = rn.choice(agent_possible_moves)
	print("Agent then moves to {} \n".format(next_agent_pos))
	x.agent_move(next_agent_pos)
	x.print_gridworld()
	agent_possible_moves = x.get_possible_moves(x.agent_position)
	print("Here are the agents possible moves from state {} : {} \n".format(x.agent_position, agent_possible_moves))

