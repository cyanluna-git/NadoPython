import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, rfft, rfftfreq

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

line, = ax.semilogx(x, np.random.rand(CHUNK))
ax.set_ylim(0 , 10000000)
ax.set_xlim(20, 4000)
while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    # pyaudio.paInt16 is signed 16bit binary string ranging from -32768 to 32767
    # thus used 'h'(unsigned 2 bytes integer) to unpack binary data
    data_int = np.array(struct.unpack(str(CHUNK) + 'h', data), dtype = 'int16')
    N = CHUNK
    yf = rfft(data_int)
    xf = rfftfreq(CHUNK, 1 / RATE)
    line.set_xdata(xf)
    line.set_ydata(np.abs(yf))
    plt.pause(0.0001)


