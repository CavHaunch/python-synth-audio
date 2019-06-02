"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys
import numpy as np
import matplotlib.pyplot as plt
import struct

CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[2], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
data = wf.readframes(CHUNK)
# play stream (3)
i = 0
while len(data) > 0:
    if i == 0:
        fmt = '<{}h'.format(wf.getnchannels()*CHUNK)
        a = struct.unpack(fmt,data)
        # a = list(a)
        a = np.array(a)
        b = a[0::2]
        c = a[1::2]
        plt.figure(1)
        plt.scatter(np.arange(len(b)), b)
        plt.scatter(np.arange(len(c)), c)
        plt.show()
    stream.write(data)
    data = wf.readframes(CHUNK)
    i = i+1

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()