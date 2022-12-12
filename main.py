# Algebra app for graphing functions
# Author: Gregory Navasarkian

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


class Function:
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


def main():

    print("\nWelcome to the Algebra app for graphing functions!")

    while True:
        print("\nPlease enter the function you would like to graph.")
        print("1. Linear")
        print("2. Quadratic")
        print("3. Cubic")
        print("4. Exponential")
        print("5. Logarithmic")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            m = float(input("Enter the slope: "))
            b = float(input("Enter the y-intercept: "))
            graph = Function().linear(m, b)
            graph.plot()

        elif choice == "2":
            a = float(input("Enter the coefficient of x^2: "))
            b = float(input("Enter the coefficient of x: "))
            c = float(input("Enter the constant: "))
            graph = Function().quadratic(a, b, c)
            graph.plot()

        elif choice == "3":
            a = float(input("Enter the coefficient of x^3: "))
            b = float(input("Enter the coefficient of x^2: "))
            c = float(input("Enter the coefficient of x: "))
            d = float(input("Enter the constant: "))
            graph = Function().cubic(a, b, c, d)
            graph.plot()

        elif choice == "4":
            a = float(input("Enter the coefficient of b^x: "))
            b = float(input("Enter the base: "))
            graph = Function().exponential(a, b)
            graph.plot()

        elif choice == "5":
            b = float(input("Enter the base (enter 0 for natural log(ln)): "))
            if (b < 0) or (b == 1):
                print("Invalid base.")
            if b == 0:
                graph = Function().logarithmic(math.e)
            else:
                graph = Function().logarithmic(b)
            graph.plot()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
