import numpy as np
import matplotlib.pyplot as plt

def main():
    """Find stationary points of x^3+y^3 on the ellipse x^2+2y^2=3"""

    # Generate ellipse polar coordinates
    theta=np.linspace(-np.pi,np.pi,1000)
    r=np.sqrt(3.0/(np.cos(theta)**2+2.0*np.sin(theta)**2))

    # Convert to cartesian
    x=r*np.cos(theta)
    y=r*np.sin(theta)

    # Calculate objective function
    z=x**3+y**3

    # Plot ellipse with colour as value of objective function
    plt.scatter(x,y,c=z,cmap="coolwarm")
    plt.show()

    # Plot value of objective with theta
    plt.plot(theta/np.pi,z)
    plt.show()

main()