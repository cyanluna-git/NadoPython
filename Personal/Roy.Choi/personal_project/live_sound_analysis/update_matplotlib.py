'''
import matplotlib.pyplot as plt
import numpy as np
plt.ion()
x = np.arange(0, 4*np.pi, 0.1)
y = [np.sin(i) for i in x]
while True:
    plt.plot(x, y, 'g-', linewidth=1.5, markersize=4)
    plt.pause(0.0001)
    plt.plot(x, [i**2 for i in y], 'g-', linewidth=1.5, markersize=4)
    plt.pause(0.0001)
    plt.plot(x, [i**2*i+0.25 for i in y], 'r-', linewidth=1.5, markersize=4)
    plt.pause(0.0001)
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10 * np.pi, 100)
y = np.sin(x)

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'b-')

while True:
    for phase in np.linspace(0, 10 * np.pi, 100):
        line1.set_ydata(np.sin(0.5 * x + phase))
        plt.pause(0.0001)