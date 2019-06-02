import sys
import numpy as np
import struct
import pyaudio

CHUNK = 1*1024

def OpenStream(wf):
    global CHUNK
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    for_mat=p.get_format_from_width(wf.getsampwidth())

    # read data
    data = wf.readframes(CHUNK)
    return data, stream, p

def play(data, stream, wf):
    global CHUNK
    # play stream (3)
    stream.write(data)
    data = wf.readframes(CHUNK)
    return data, stream, wf

def stop(stream, p):
    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()