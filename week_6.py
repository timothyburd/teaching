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
stat_points = [(-1, -2), (-1, 2), (1, -2), (1, 2)]
ax.scatter(*zip(*stat_points), s=10, marker="o")
ax.set_title('1a')
plt.savefig("week6_1a.pdf")
plt.show()



# 1b
x = np.arange(-1.5, 1.5, delta)
y = np.arange(-1.5, 1.5, delta)
X, Y = np.meshgrid(x, y)#
Z = X**4 + 2 * X*X*Y*Y - Y*Y*Y*Y - 2 * X*X + 3
fig, ax = plt.subplots(figsize=(8, 6))
CS = ax.contour(X, Y, Z, 30)
ax.clabel(CS, inline=1, fontsize=10)
stat_points = [(-1, 0), (-1.0/np.sqrt(2), -1.0/np.sqrt(2)), (-1.0/np.sqrt(2), 1.0/np.sqrt(2)), (0, 0), (1.0/np.sqrt(2), -1.0/np.sqrt(2)), (1.0/np.sqrt(2), 1.0/np.sqrt(2)), (1, 0)]
ax.scatter(*zip(*stat_points), s=10, marker="o")
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

# 4
num_pnts = 1000
theta = np.linspace(-np.pi,np.pi,num_pnts)
cos_theta = np.cos(theta)
sin_theta = np.sin(theta)
quad_soln = lambda a,b,c: (-b+np.sqrt(b*b-4*a*c))/(2*a)
r = quad_soln(cos_theta**2+4*sin_theta**2,-2*cos_theta,-3)
fig, ax = plt.subplots()
ax.plot(theta/np.pi,r)
ax.set_title('4')
ax.set_xlabel(r'$\theta$ / $\pi$')
ax.set_ylabel(r'$r$')
plt.savefig("week6_4.pdf")
plt.show()


