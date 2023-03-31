# Algebra app for graphing functions
# Author: Gregory Navasarkian

import customtkinter as ctk
import math
from functions import Functions


def linear_window():
    def graph():
        m = float(m_entry.get())
        b = float(b_entry.get())
        graph = Functions().linear(m, b)
        graph.plot()
    
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Linear Functions")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Linear Functions", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the slope and y-intercept below ( y = Mx + B )", font=("Arial", 16))
    description.pack(pady=8)

    m_label = ctk.CTkLabel(app, text="M: ", font=("Arial", 16))
    m_label.pack(pady=8)

    m_entry = ctk.CTkEntry(app, font=("Arial", 16))
    m_entry.pack(pady=8)
    
    b_label = ctk.CTkLabel(app, text="B: ", font=("Arial", 16))
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
        graph = Functions().quadratic(a, b, c)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Quadratic Functions")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Quadratic Functions", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the coefficients below ( y = Ax^2 + Bx + C )", font=("Arial", 16))
    description.pack(pady=8)

    a_label = ctk.CTkLabel(app, text="A: ", font=("Arial", 16))
    a_label.pack(pady=8)

    a_entry = ctk.CTkEntry(app, font=("Arial", 16))
    a_entry.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="B: ", font=("Arial", 16))
    b_label.pack(pady=8)

    b_entry = ctk.CTkEntry(app, font=("Arial", 16))
    b_entry.pack(pady=8)

    c_label = ctk.CTkLabel(app, text="C: ", font=("Arial", 16))
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
        graph = Functions().cubic(a, b, c, d)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x550")
    app.title("Cubic Functions")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Cubic Functions", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the coefficients below ( y = Ax^3 + Bx^2 + Cx + D )", font=("Arial", 16))
    description.pack(pady=8)

    a_label = ctk.CTkLabel(app, text="A: ", font=("Arial", 16))
    a_label.pack(pady=8)

    a_entry = ctk.CTkEntry(app, font=("Arial", 16))
    a_entry.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="B: ", font=("Arial", 16))
    b_label.pack(pady=8)

    b_entry = ctk.CTkEntry(app, font=("Arial", 16))
    b_entry.pack(pady=8)

    c_label = ctk.CTkLabel(app, text="C: ", font=("Arial", 16))
    c_label.pack(pady=8)

    c_entry = ctk.CTkEntry(app, font=("Arial", 16))
    c_entry.pack(pady=8)

    d_label = ctk.CTkLabel(app, text="D: ", font=("Arial", 16))
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
        graph = Functions().exponential(a, b)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Exponential Functions")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Exponential Functions", font=("Arial", 24))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the base and coefficient below ( y = A * B^x )", font=("Arial", 16))
    description.pack(pady=8)

    a_label = ctk.CTkLabel(app, text="A: ", font=("Arial", 16))
    a_label.pack(pady=8)

    a_entry = ctk.CTkEntry(app, font=("Arial", 16))
    a_entry.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="B: ", font=("Arial", 16))
    b_label.pack(pady=8)

    b_entry = ctk.CTkEntry(app, font=("Arial", 16))
    b_entry.pack(pady=8)

    graph_button = ctk.CTkButton(
        app, text="Graph", command=graph, font=("Arial", 18), width=400, height=30)
    graph_button.pack(pady=15)

    app.mainloop()


def logarithmic_window():
    def graph():
        b = float(b_entry.get())
        if b == 0:
            graph = Functions().logarithmic(math.e)
        else:
            graph = Functions().logarithmic(b)
        graph.plot()

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Logarithmic Functions")
    app.resizable(False, False)

    title = ctk.CTkLabel(app, text="Logarithmic Functions", font=("Arial", 28))
    title.pack(pady=10)

    description = ctk.CTkLabel(
        app, text="Enter the base below (enter 0 for natural log)", font=("Arial", 16))
    description.pack(pady=8)

    b_label = ctk.CTkLabel(app, text="Base: ", font=("Arial", 16))
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
