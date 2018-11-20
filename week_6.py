import numpy as np
import matplotlib.pyplot as plt

"""
Week 6 problems, question 1 plots
"""

delta = 0.025



# 1a
x = np.arange(-4.0, 4.0, delta)
y = np.arange(-4.0, 4.0, delta)
X, Y = np.meshgrid(x, y)#
Z = X*X*X + Y*Y*Y - 3 * X -12*Y +20
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 10)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('1a')
plt.savefig("week6_1a.pdf")
plt.show()



# 1b
x = np.arange(-1.5, 1.5, delta)
y = np.arange(-1.5, 1.5, delta)
X, Y = np.meshgrid(x, y)#
Z = X**4 + 2 * X*X*Y*Y - Y*Y*Y*Y - 2 * X*X + 3
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 30)
# ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('1b')
plt.savefig("week6_1b.pdf")
plt.show()




# 1c
x = np.arange(-4.0, 4.0, delta)
y = np.arange(-4.0, 4.0, delta)
X, Y = np.meshgrid(x, y)
Z = np.cos(X + Y)
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 10)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('1c')
plt.savefig("week6_1c.pdf")
plt.show()

# 2

x = np.arange(-1.5, 1.5, delta)
y = np.arange(-1.5, 1.5, delta)
X, Y = np.meshgrid(x, y)
Z = 2 * X * Y
constraint = X*X + Y*Y
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z, 30)
CS = ax.contour(X, Y, constraint, [1])
plt.axis('equal')
ax.set_title('1c')
plt.savefig("week6_2.pdf")
plt.show()