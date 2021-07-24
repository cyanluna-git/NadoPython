import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = CHUNK
)


fig, ax = plt.subplots()
x = np.arange(0, CHUNK, 1)

line, = ax.plot(x, np.random.rand(CHUNK))
ax.set_ylim(-30000 , 30000)
ax.set_xlim(0, CHUNK)
while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    # pyaudio.paInt16 is signed 16bit binary string ranging from -32768 to 32767
    # thus used 'h'(unsigned 2 bytes integer) to unpack binary data
    data_int = np.array(struct.unpack(str(CHUNK) + 'h', data), dtype = 'int16')
    line.set_ydata(data_int)
    plt.pause(0.0001)


