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
        app, text="Enter the slope and y-intercept below ( y = mx + b )", font=("Arial", 16))
    description.pack(pady=8)

    m_label = ctk.CTkLabel(app, text="m: ", font=("Arial", 16))
    m_label.pack(pady=8)

    m_entry = ctk.CTkEntry(app, font=("Arial", 16))
    m_entry.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="b: ", font=("Arial", 16))
    b_label.pack(pady=8)

    b_entry = ctk.CTkEntry(app, font=("Arial", 16))
    b_entry.pack(pady=8)

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
        app, text="Enter the coefficients below ( y = ax^2 + bx + c )", font=("Arial", 16))
    description.pack(pady=8)

    a_label = ctk.CTkLabel(app, text="a: ", font=("Arial", 16))
    a_label.pack(pady=8)

    a_entry = ctk.CTkEntry(app, font=("Arial", 16))
    a_entry.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="b: ", font=("Arial", 16))
    b_label.pack(pady=8)

    b_entry = ctk.CTkEntry(app, font=("Arial", 16))
    b_entry.pack(pady=8)

    c_label = ctk.CTkLabel(app, text="c: ", font=("Arial", 16))
    c_label.pack(pady=8)

    c_entry = ctk.CTkEntry(app, font=("Arial", 16))
    c_entry.pack(pady=8)

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
        app, text="Enter the coefficients below ( y = ax^3 + bx^2 + cx + d )", font=("Arial", 16))
    description.pack(pady=8)

    a_label = ctk.CTkLabel(app, text="a: ", font=("Arial", 16))
    a_label.pack(pady=8)

    a_entry = ctk.CTkEntry(app, font=("Arial", 16))
    a_entry.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="b: ", font=("Arial", 16))
    b_label.pack(pady=8)

    b_entry = ctk.CTkEntry(app, font=("Arial", 16))
    b_entry.pack(pady=8)

    c_label = ctk.CTkLabel(app, text="c: ", font=("Arial", 16))
    c_label.pack(pady=8)

    c_entry = ctk.CTkEntry(app, font=("Arial", 16))
    c_entry.pack(pady=8)

    d_label = ctk.CTkLabel(app, text="d: ", font=("Arial", 16))
    d_label.pack(pady=8)

    d_entry = ctk.CTkEntry(app, font=("Arial", 16))
    d_entry.pack(pady=8)

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
        app, text="Enter the base and coefficient below ( y = a * b^x )", font=("Arial", 16))
    description.pack(pady=8)

    a_label = ctk.CTkLabel(app, text="a: ", font=("Arial", 16))
    a_label.pack(pady=8)

    a_entry = ctk.CTkEntry(app, font=("Arial", 16))
    a_entry.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="b: ", font=("Arial", 16))
    b_label.pack(pady=8)

    b_entry = ctk.CTkEntry(app, font=("Arial", 16))
    b_entry.pack(pady=8)

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

    title = ctk.CTkLabel(app, text="Logarithmic Function", font=("Arial", 28))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the base below (enter 0 for natural log)", font=("Arial", 16))
    description.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="base: ", font=("Arial", 16))
    b_label.pack(pady=8)

    b_entry = ctk.CTkEntry(app, font=("Arial", 16))
    b_entry.pack(pady=8)

    graph_button = ctk.CTkButton(
        app, text="Graph", command=graph, font=("Arial", 18), width=400, height=30)
    graph_button.pack(pady=15)

    app.mainloop()


def main():

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x350")
    app.title("Algebra App")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Algebra App", font=("Arial", 28))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Select a function type to graph below", font=("Arial", 18))
    description.pack(pady=8)

    linear_button = ctk.CTkButton(app, text="Linear", command=linear_window, font=(
        "Arial", 18), width=400, height=30)
    linear_button.pack(pady=8)

    quadratic_button = ctk.CTkButton(
        app, text="Quadratic", command=quadratic_window, font=("Arial", 18), width=400, height=30)
    quadratic_button.pack(pady=8)

    cubic_button = ctk.CTkButton(app, text="Cubic", command=cubic_window, font=(
        "Arial", 18), width=400, height=30)
    cubic_button.pack(pady=8)

    exponential_button = ctk.CTkButton(
        app, text="Exponential", command=exponential_window, font=("Arial", 18), width=400, height=30)
    exponential_button.pack(pady=8)

    logarithmic_button = ctk.CTkButton(
        app, text="Logarithmic", command=logarithmic_window, font=("Arial", 18), width=400, height=30)
    logarithmic_button.pack(pady=8)

    app.mainloop()


if __name__ == '__main__':
    main()
