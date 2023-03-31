import math
from graph import Graph

class Functions:
    """
    Class for functions
    """

    def linear(self, m, b):
        """
        Linear function
        """
        x = range(-8, 8)
        y = [m * i + b for i in x]
        return Graph(x, y)

    def quadratic(self, a, b, c):
        """
        Quadratic function
        """
        x = range(-8, 8)
        y = [a * i ** 2 + b * i + c for i in x]
        return Graph(x, y)

    def cubic(self, a, b, c, d):
        """
        Cubic function
        """
        x = range(-8, 8)
        y = [a * i ** 3 + b * i ** 2 + c * i + d for i in x]
        return Graph(x, y)

    def exponential(self, a, b):
        """
        Exponential function
        """
        x = range(-4, 8)
        y = [a * b ** i for i in x]
        return Graph(x, y)

    def logarithmic(self, b):
        """
        Logarithmic function
        """
        x = range(1, 15)
        y = [math.log(i, b) for i in x]
        return Graph(x, y)
