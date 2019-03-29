import numpy as np
import random

def update_sample_mean(mean, number_of_samples, new_sample):
	
	updated_mean = float(mean) + ((float(new_sample) - float(mean))/float(number_of_samples+1))
	
	return float(updated_mean)


### Trashcode



#to initiate a class instanec with data do as follows:
#class Lol:
#	def __init__(self, meme):
#		self.image = meme

# x = Lol(funnycat.jpg)


#for plotting:
#import matplotlib.pyplot as plt
#plt.plot(*)
#plt.plot(value, label='*') #<- its the axis name
#plt.xscale('') 
#plt.legend()
#plt.show()

#import matplotlib.pyplot as plt

#temp = 0

#for i in range(0, 15):
#	temp += i
#	plt.plot(i, temp, 'r+')
#
#plt.xlabel("Iterations")
#plt.ylabel("Sum")
#plt.xscale('log')
#plt.legend()
#plt.show()