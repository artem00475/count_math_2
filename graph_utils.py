import matplotlib.pyplot as plt
import numpy as np
from sympy import *


# Отображения графика уравнения
def show_graph(a, b, num):
    x = np.arange(a, b + 0.01, 0.01)
    if num == 1:
        plt.plot(x, x ** 3 - 0.77 * x ** 2 - 1.251 * x + 0.43)
    elif num == 2:
        plt.plot(x, x ** 2 - x + 4)
    elif num == 3:
        plt.plot(x, 20 * np.cos(x) + x ** 2)
    plt.grid(True)
    plt.show()


# Отображения графика системы уравнений
def show_system_graph(num):
    var('x y')
    if num == 1:
        p1 = plot_implicit(Eq(0.1 * x ** 2 + x + 0.2 * y ** 2, 0.3), show=False, line_color='r')
        p2 = plot_implicit(Eq(0.2 * x ** 2 + y + 0.1 * x * y, 0.7), show=False)
    else:
        p1 = plot_implicit(Eq(0.2 * x ** 2 + x + 0.3 * y ** 2, 0.5), show=False, line_color='r')
        p2 = plot_implicit(Eq(0.4 * x ** 2 + y + 0.2 * x * y, 0.5), show=False)
    p2.extend(p1)
    p2.xscale = ''
    p2.show()
