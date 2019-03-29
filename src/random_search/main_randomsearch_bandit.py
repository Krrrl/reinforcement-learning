from env.bandit import Bandit
from random_search.bandit_player import BanditPlayer


print("Lets play some bandits\n")
number_of_bandits = int(input("How many bandits should we play?\n"))

x = BanditPlayer(number_of_bandits)

number_of_plays = int(input("How many times should we play?\n"))
epsilon = float(input("What is our epsilon?\n"))

x.play_bandits_comp_random(epsilon, number_of_plays)