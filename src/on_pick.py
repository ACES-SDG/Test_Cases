import matplotlib.pyplot as ax
import numpy as np
from numpy.random import rand
# from matplotlib.figure import Figure as fig
import matplotlib.pyplot as plt
from matplotlib.backend_bases import FigureCanvasBase 

fig = plt.figure()

ax.plot(rand(100), 'o', picker=5)  # 5 points tolerance

plt.show()
def on_pick(event):
    line = event.artist
    xdata, ydata = line.get_data()
    ind = event.ind
    print('on pick line:', np.array([xdata[ind], ydata[ind]]).T)

cid = fig.canvas.mpl_connect('pick_event', on_pick)