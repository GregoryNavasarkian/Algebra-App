from matplotlib import pyplot as plt
import math

class Graph:
	"""
	Class for graphing functions
	"""

	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def plot(self):
		fig = plt.figure(figsize=(15, 12))
		plt.xticks(range(min(self.x), max(self.x) + 1))
		ax = fig.add_subplot(111)
		
		plt.plot(self.x, self.y)
		ax.spines['top'].set_color('none')
		ax.spines['right'].set_color('none')
		ax.spines['bottom'].set_position('zero')
		ax.spines['left'].set_position('zero')

		plt.scatter(0, 0)
		
		plt.grid(True)
		plt.show()
