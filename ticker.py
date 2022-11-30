import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import numpy as np


x = np.linspace(0, 10, 1000)
y = 0.000001 * np.sin(10 * x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y)

def y_fmt(x, y):
	return '{:2.2e}'.format(x).replace('e', 'x10^')

ax.yaxis.set_major_formatter(tick.FuncFormatter(y_fmt))

plt.show()
