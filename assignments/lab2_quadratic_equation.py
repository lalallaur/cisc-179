import math
import numpy as np # sed for mathematical operations
import matplotlib.pyplot as plt # used for plotting graphs

def solve_quadratic(a, b, c);
    discriminant = b**2 - 4*a*c

    if discriminant > 0;
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, None # returns single roots
    else:
        return None, None #if it is negative?

    def plot_quadratic(a, b, c);
        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        plt.plot(x, y) #plots equation on graph
        plt.title("Quadratic Equation") # title
        plt.axhline(0, color='black', linewidth=1) # y axis
        plt.axvline(0, color='black', linewidth=1) # x axis
        plt.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

# the values inputted
a = -1
b = 5
c = 0

plot_quadratic(a, b, c) # calls function to plot the quadratic equatio
