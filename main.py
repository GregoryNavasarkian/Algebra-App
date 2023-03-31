# Algebra app for graphing functions
# Author: Gregory Navasarkian

from matplotlib import pyplot as plt
import math
import tkinter as tk
import customtkinter as ctk


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


def linear_window():
    def graph():
        m = float(m_entry.get())
        b = float(b_entry.get())
        graph = Function().linear(m, b)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Linear Function")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Linear Function", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the slope and y-intercept below", font=("Arial", 16))
    description.pack(pady=5)

    m_label = ctk.CTkLabel(app, text="Slope: ", font=("Arial", 14))
    m_label.pack(pady=5)

    m_entry = ctk.CTkEntry(app, font=("Arial", 14))
    m_entry.pack(pady=5)

    b_label = ctk.CTkLabel(app, text="Y-intercept: ", font=("Arial", 14))
    b_label.pack(pady=5)

    b_entry = ctk.CTkEntry(app, font=("Arial", 14))
    b_entry.pack(pady=5)

    graph_button = ctk.CTkButton(
        app, text="Graph", command=graph, font=("Arial", 18), width=400, height=30)
    graph_button.pack(pady=15)

    app.mainloop()


def quadratic_window():
    def graph():
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        graph = Function().quadratic(a, b, c)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Quadratic Function")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Quadratic Function", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the coefficients below", font=("Arial", 16))
    description.pack(pady=5)

    a_label = ctk.CTkLabel(app, text="a: ", font=("Arial", 14))
    a_label.pack(pady=5)

    a_entry = ctk.CTkEntry(app, font=("Arial", 14))
    a_entry.pack(pady=5)

    b_label = ctk.CTkLabel(app, text="b: ", font=("Arial", 14))
    b_label.pack(pady=5)

    b_entry = ctk.CTkEntry(app, font=("Arial", 14))
    b_entry.pack(pady=5)

    c_label = ctk.CTkLabel(app, text="c: ", font=("Arial", 14))
    c_label.pack(pady=5)

    c_entry = ctk.CTkEntry(app, font=("Arial", 14))
    c_entry.pack(pady=5)

    graph_button = ctk.CTkButton(
        app, text="Graph", command=graph, font=("Arial", 18), width=400, height=30)
    graph_button.pack(pady=15)

    app.mainloop()


def cubic_window():
    def graph():
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        d = float(d_entry.get())
        graph = Function().cubic(a, b, c, d)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Cubic Function")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Cubic Function", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the coefficients below", font=("Arial", 16))
    description.pack(pady=5)

    a_label = ctk.CTkLabel(app, text="a: ", font=("Arial", 14))
    a_label.pack(pady=5)

    a_entry = ctk.CTkEntry(app, font=("Arial", 14))
    a_entry.pack(pady=5)

    b_label = ctk.CTkLabel(app, text="b: ", font=("Arial", 14))
    b_label.pack(pady=5)

    b_entry = ctk.CTkEntry(app, font=("Arial", 14))
    b_entry.pack(pady=5)

    c_label = ctk.CTkLabel(app, text="c: ", font=("Arial", 14))
    c_label.pack(pady=5)

    c_entry = ctk.CTkEntry(app, font=("Arial", 14))
    c_entry.pack(pady=5)

    d_label = ctk.CTkLabel(app, text="d: ", font=("Arial", 14))
    d_label.pack(pady=5)

    d_entry = ctk.CTkEntry(app, font=("Arial", 14))
    d_entry.pack(pady=5)

    graph_button = ctk.CTkButton(
        app, text="Graph", command=graph, font=("Arial", 18), width=400, height=30)
    graph_button.pack(pady=15)

    app.mainloop()


def exponential_window():
    def graph():
        a = float(a_entry.get())
        b = float(b_entry.get())
        graph = Function().exponential(a, b)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Exponential Function")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Exponential Function", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the coefficients below", font=("Arial", 16))
    description.pack(pady=5)

    a_label = ctk.CTkLabel(app, text="a: ", font=("Arial", 14))
    a_label.pack(pady=5)

    a_entry = ctk.CTkEntry(app, font=("Arial", 14))
    a_entry.pack(pady=5)

    b_label = ctk.CTkLabel(app, text="b: ", font=("Arial", 14))
    b_label.pack(pady=5)

    b_entry = ctk.CTkEntry(app, font=("Arial", 14))
    b_entry.pack(pady=5)

    graph_button = ctk.CTkButton(
        app, text="Graph", command=graph, font=("Arial", 18), width=400, height=30)
    graph_button.pack(pady=15)

    app.mainloop()


def logarithmic_window():
    def graph():
        a = float(a_entry.get())
        b = float(b_entry.get())
        graph = Function().logarithmic(a, b)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Logarithmic Function")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Logarithmic Function", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the coefficients below", font=("Arial", 16))
    description.pack(pady=5)

    a_label = ctk.CTkLabel(app, text="a: ", font=("Arial", 14))
    a_label.pack(pady=5)

    a_entry = ctk.CTkEntry(app, font=("Arial", 14))
    a_entry.pack(pady=5)

    b_label = ctk.CTkLabel(app, text="b: ", font=("Arial", 14))
    b_label.pack(pady=5)

    b_entry = ctk.CTkEntry(app, font=("Arial", 14))
    b_entry.pack(pady=5)

    graph_button = ctk.CTkButton(
        app, text="Graph", command=graph, font=("Arial", 18), width=400, height=30)
    graph_button.pack(pady=15)

    app.mainloop()


def main():

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Algebra App")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Algebra App", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Select a function type to graph below", font=("Arial", 16))
    description.pack(pady=5)
    
    linear_button = ctk.CTkButton(app, text="Linear", command=linear_window, font=(
        "Arial", 18), width=400, height=30)
    linear_button.pack(pady=5)

    quadratic_button = ctk.CTkButton(
        app, text="Quadratic", command=quadratic_window, font=("Arial", 18), width=400, height=30)
    quadratic_button.pack(pady=5)

    cubic_button = ctk.CTkButton(app, text="Cubic", command=cubic_window, font=(
        "Arial", 18), width=400, height=30)
    cubic_button.pack(pady=5)

    exponential_button = ctk.CTkButton(
        app, text="Exponential", command=exponential_window, font=("Arial", 18), width=400, height=30)
    exponential_button.pack(pady=5)

    logarithmic_button = ctk.CTkButton(
        app, text="Logarithmic", command=logarithmic_window, font=("Arial", 18), width=400, height=30)
    logarithmic_button.pack(pady=5)

    app.mainloop()

    # print("\nWelcome to the Algebra app for graphing functions!")

    # while True:
    #     print("\nPlease enter the function you would like to graph.")
    #     print("1. Linear")
    #     print("2. Quadratic")
    #     print("3. Cubic")
    #     print("4. Exponential")
    #     print("5. Logarithmic")
    #     print("6. Exit")

    #     choice = input("\nEnter your choice: ")

    #     if choice == "1":
    #         m = float(input("Enter the slope: "))
    #         b = float(input("Enter the y-intercept: "))
    #         graph = Function().linear(m, b)
    #         graph.plot()

    #     elif choice == "2":
    #         a = float(input("Enter the coefficient of x^2: "))
    #         b = float(input("Enter the coefficient of x: "))
    #         c = float(input("Enter the constant: "))
    #         graph = Function().quadratic(a, b, c)
    #         graph.plot()

    #     elif choice == "3":
    #         a = float(input("Enter the coefficient of x^3: "))
    #         b = float(input("Enter the coefficient of x^2: "))
    #         c = float(input("Enter the coefficient of x: "))
    #         d = float(input("Enter the constant: "))
    #         graph = Function().cubic(a, b, c, d)
    #         graph.plot()

    #     elif choice == "4":
    #         a = float(input("Enter the coefficient of b^x: "))
    #         b = float(input("Enter the base: "))
    #         graph = Function().exponential(a, b)
    #         graph.plot()

    #     elif choice == "5":
    #         b = float(input("Enter the base (enter 0 for natural log(ln)): "))
    #         if (b < 0) or (b == 1):
    #             print("Invalid base.")
    #         if b == 0:
    #             graph = Function().logarithmic(math.e)
    #         else:
    #             graph = Function().logarithmic(b)
    #         graph.plot()

    #     elif choice == "6":
    #         break

    #     else:
    #         print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
