import numpy as np
import random as rn
from copy import deepcopy

LENGTH = 3

class TicTacToe_Agent:



	def __init__(self, learning_rate):
		self.VF = {}
		self.learning_rate = learning_rate


		self.playerID = -1
		self.game_state_history = []


	def set_playerID(self, playerID):
		self.playerID = playerID
		print("PlayerID set to: {} \n".format(self.playerID))

	def get_all_possible_states(self, board_state, row, col):
		possible_states = {}

		


	def init_VF(self, possible_states):
		#initialize VF
		pass

	



	def find_possible_moves(self, board_state):
		
		possible_moves = []

		for i in range(0, LENGTH):
			for j in range(0, LENGTH):
				if(board_state[i][j] == 0):
					possible_moves.append((i,j))

		return possible_moves

	def hash_state(board_state):
		
		hash_value = 0
		power_counter = 0
		
		for i in range(0, LENGTH):
			for j in range(0, LENGTH):
				
				if(board_state[i][j] == 0.):
					v = 0
				
				elif(board_state[i][j] == 1.):
					v = 1

				elif(board_state[i][j] == 2.):
					v = 2

				hash_value += (3**power_counter) * v
				power_counter += 1

		return hash_value

	def reconstruct_from_hash(self, hash_value):
		
		board_state = np.zeros((LENGTH, LENGTH))

		power_counter = LENGTH*LENGTH-1

		for i in range(0, LENGTH):
			for j in range(0, LENGTH):
				
				current_pos_state = (hash_value//(np.power(3, power_counter))) 
			
				board_state[2-i][2-j] = current_pos_state
				hash_value -= current_pos_state*(3**power_counter)

				power_counter -= 1

		return board_state

	def get_next_state(self, hash, move):

		board_state = self.reconstruct_from_hash(hash)
		board_state[move[0]][move[1]] = self.playerID
		next_hash = hash_state(board_state)

		return next_hash


	def update_VF(self, env, result):
		
		#V(s) = V(s) + learning_rate*(V(s') - V(s))


		hash_value = self.hash_state(env)

		self.VF[hash_value] = result

	def next_move(self, board_state):

		possible_moves = self.find_possible_moves(env)

		if(rn.random() > self.learning_rate):

			next_move = possible_moves[rn.randint(len(possible_moves))]
			row = next_move[0]
			col = next_move[1]
			
			return row, col

		for i in range(0, len(possible_moves)):
			high_val = 

		hash_value = self.hash_state(env)


		if(hash_value in self.VF):
			pass

	def update_VF(self):
		pass
