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
        plt.title("Graph of f(x)")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")

        plt.grid()
        plt.plot(self.x, self.y)
        plt.show()
