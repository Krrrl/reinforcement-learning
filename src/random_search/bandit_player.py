import numpy as np
import random

from env.bandit import Bandit
from custom_lib.magicHat import update_sample_mean


class BanditPlayer:

	number_of_machines = 0
	machine_name = "machine"
	bandit_list = []

	def __init__(self, number_of_machines):
		self.number_of_machines = number_of_machines
		print("I am agent, I play {} bandit machines\n".format(number_of_machines))

		self.setup_bandits()

	def setup_bandits(self):
		for i in range(0, self.number_of_machines):
			name = self.machine_name + str(i)
			probability = random.random()
			name = Bandit(probability)
			self.bandit_list = np.append(self.bandit_list, name)

	def play_bandits_random_search(self, epsilon, number_of_plays):
		
		number_of_samples = np.zeros(self.number_of_machines)
		win_probabilities = np.zeros(self.number_of_machines)
		number_of_wins = np.zeros(self.number_of_machines)


		for i in range(0, number_of_plays):

			if(random.random() > epsilon):
				machine_number = np.argmax(win_probabilities)

			else:
				machine_number = random.randint(0, (self.number_of_machines-1))
			

			#chosen_machine = self.machine_name + str(machine_number)
			
			outcome = self.bandit_list[machine_number].pull_arm()
			number_of_wins[machine_number] += outcome

			win_probabilities[machine_number] = update_sample_mean(win_probabilities[machine_number], 
																	number_of_samples[machine_number],
																	outcome)
			number_of_samples[machine_number] += 1


		print("I played {} times with a total of {} wins, and found the following winning probabilities: \n".format(number_of_plays, 
																													(np.sum(number_of_wins))))
		for i in range(0,self.number_of_machines):
			chosen_machine = self.machine_name + str(i)
			print("{} had a winning probability of {:.3f} as far as I know. I played it {} times \n".format(chosen_machine, 
																											win_probabilities[i], 
																											number_of_samples[i]))

	def play_bandits_comp_random(self, epsilon, number_of_plays):

		self.play_bandits_random_search(epsilon, number_of_plays)
		print("For comparison, here is me playing {} times randomly: \n".format(number_of_plays))
		self.play_bandits_random_search(1.01, number_of_plays)
