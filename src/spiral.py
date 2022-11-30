import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 

n = 256
angle = np.linspace(0,12*2*np.pi, n)
radius = np.linspace(.5,1.,n)

x = radius * np.cos(angle)
y = radius * np.sin(angle)

plt.scatter(x,y,c = angle, cmap = cm.hsv)
plt.show()