import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 1000)

def lemniscate(a,theta):
    x = a * np.sqrt(2)*np.cos(theta)/(1 + np.sin(theta)**2)
    y = x * np.sin(theta)
    return x , y

x,y = lemniscate(2,theta)

plt.plot(x, y,linewidth=12,color='gold')
plt.axis('equal')
plt.title('Lemniscate Curve')
plt.show()
