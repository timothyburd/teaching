import numpy as np
import matplotlib.pyplot as plt

def main():
    delta = 0.0025

    x = np.arange(-4.0, 4.0, delta)
    y = np.arange(-4.0, 4.0, delta)

    constrained_xs = np.arccos(y*y) - y



    X, Y = np.meshgrid(x, y)  #
    Z = X * X * X - 3 * X * Y + Y*Y*Y
    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z, 20)
    ax.clabel(CS, inline=1, fontsize=10)
    stat_points = [(0, 0), (1, 1)]
    ax.scatter(*zip(*stat_points), s=10, marker="o")
    ax.plot(x, constrained_xs, label='constraint')
    plt.savefig("question_11_collection_hilary_2020.pdf")
    plt.show()




    pass


if __name__ == '__main__':

    main()