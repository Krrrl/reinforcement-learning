import numpy as np 


class TicTacToe_Game:
#Takes a row,col from one of two alternating players. 
#Returns 0, 1 or 2 for draw, player1 victory or player2 victory respectively.

	def __init__(self):
		self.board = np.zeros((3,3))
		self.nr_of_moves = 0
		self.player1SYM = 1
		self.player2SYM = 2
		self.game_winner = -1
		print("Game created! Good luck!\n")


	def get_square(self, row, col):
		return self.board[row, col]

	def get_board_state(self):
		return self.board
	
	def check_winner(self):

		for i in range(0,3):

			if((self.board[i, 0] == self.board[i, 1] == self.board[i, 2] != 0.)
				or (self.board[0, i] == self.board[1, i] == self.board[2, i] != 0.)
				or (self.board[0, 0] == self.board[1, 1] == self.board[2, 2] != 0.)
				or (self.board[0, 2] == self.board[1, 1] == self.board[2, 0] != 0.)
				):
				print("We have a winner!\n")
				return True

		return False
		

	def game_draw(self):
		print("It's a draw!\n")
		self.game_winner = 0
		return 0

	def place_marker(self, row, col):
		playerID = 0.
		if((self.nr_of_moves % 2) == 0):
			playerID = self.player1SYM
		else:
			playerID = self.player2SYM
			
		if(self.board[row,col] != 0.):
			print("Illegal move!\n")
			print("Go again! Do better!\n")
		else:
			self.board[row,col] = playerID
			self.nr_of_moves += 1
			print(self.get_board_state())


			if(self.check_winner()):
				print("Player {} won! \n".format(playerID))
				self.game_winner = playerID
				return playerID

		if(self.nr_of_moves == 9):
			return self.game_draw()


if __name__ == '__main__':
	from copy import deepcopy

	game1 = TicTacToe()
	game1.get_board_state()

	print("Here is how a simple game could look: \n")
	game1.place_marker(1, 1)
	game1.place_marker(0, 0)
	game1.place_marker(1, 0)
	game1.place_marker(2, 1)
	print("This is how it looks when winning: \n")
	#forking the game at current state
	game2 = deepcopy(game1)

	game1.place_marker(1, 2)
	print("Or when there is a draw: \n")
	
	game2.place_marker(2, 0)
	game2.place_marker(1, 2)
	game2.place_marker(0, 1)
	game2.place_marker(0, 2)
	game2.place_marker(2, 2)
