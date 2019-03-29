import numpy as np
#import matplotlib
import random

class Bandit:
	"""Docstring: An implementation of a one-armed-bandit. Returns 1 on win, 0 on loss."""
	win_prob = 0

	def __init__(self, win_prob):
		self.win_prob = win_prob
		print("Machine with winning probabillity: {0:.3f} created.\n".format(win_prob))

	def pull_arm(self):
		if(random.randint(0,100) <= (100*self.win_prob)): 
			return 1 
		else: 
			return 0 

