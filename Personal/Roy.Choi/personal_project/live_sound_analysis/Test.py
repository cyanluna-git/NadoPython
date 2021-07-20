import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

x = np.arange(0, 2*CHUNK, 2)
fig, ax = plt.subplots()
line, = ax.plot(x, np.random.rand(CHUNK))
plt.show()
print('yes')
while True:
    time.sleep(10)
    line, = ax.plot(x, np.random.rand(CHUNK))
    # line.set_ydata(np.random.rand(CHUNK))
    # fig.canvas.draw()
    # fig.canvas.flush_events()