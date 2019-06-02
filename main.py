import wave
import sys
import sound
from pynput.keyboard import KeyCode, Key, Controller, Listener
import threading
import time

# 

keyboard = Controller()

global play
play = False
global track
track = 0

def on_press(key):
    global play
    global track
    # print('{0} press'.format(key))
    try:
        if key == KeyCode.from_char('a'):
            play = True
            track = 0
        if key == KeyCode.from_char('w'):
            play = True
            track = 1
        if key == KeyCode.from_char('s'):
            play = True
            track = 2
        if key == KeyCode.from_char('e'):
            play = True
            track = 3
        if key == KeyCode.from_char('d'):
            play = True
            track = 4
        if key == KeyCode.from_char('f'):
            play = True
            track = 5
        if key == KeyCode.from_char('t'):
            play = True
            track = 6
        if key == KeyCode.from_char('g'):
            play = True
            track = 7
        if key == KeyCode.from_char('y'):
            play = True
            track = 8
        if key == KeyCode.from_char('h'):
            play = True
            track = 9
        if key == KeyCode.from_char('u'):
            play = True
            track = 10
        if key == KeyCode.from_char('j'):
            play = True
            track = 11
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    global play
    global track
    # print('{0} release'.format(key))
    try:
        if key == Key.esc:
            return False
        if key == KeyCode.from_char('a'):
            play = False
        if key == KeyCode.from_char('w'):
            play = False
        if key == KeyCode.from_char('s'):
            play = False
        if key == KeyCode.from_char('e'):
            play = False
        if key == KeyCode.from_char('d'):
            play = False
        if key == KeyCode.from_char('f'):
            play = False
        if key == KeyCode.from_char('t'):
            play = False
        if key == KeyCode.from_char('g'):
            play = False
        if key == KeyCode.from_char('h'):
            play = False
        if key == KeyCode.from_char('y'):
            play = False
        if key == KeyCode.from_char('h'):
            play = False
        if key == KeyCode.from_char('u'):
            play = False
        if key == KeyCode.from_char('j'):
            play = False
    except AttributeError:
        print('special key {0} pressed'.format(key))

def task():
    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf = []
    for index in range(1,len(sys.argv)):
        wf.append(wave.open(sys.argv[index], 'rb'))
        # wf.append(wave.open(wavefile, 'rb'))
    # wf[1] = wave.open(sys.argv[1], 'rb')
    channels = []
    for wavefile in wf:
        channels.append(wavefile.getnchannels())
    # channels[1]=wf[1].getnchannels()
    rate=[]
    for wavefile in wf:
        rate.append(wavefile.getframerate())
    # rate[1]=wf[1].getframerate()
    # for_mat=p.get_format_from_width(wf.getsampwidth())

    file_open = 0

# 
    try:
        global play
        global track
        data, stream, py_audio_handle = sound.OpenStream(wf[track])
        file_open = 1
        prev_track = track
        while len(data) > 0:
            if play==True and track==prev_track:
                if file_open==0:
                    data, stream, py_audio_handle = sound.OpenStream(wf[track])
                    file_open = 1
                data, stream, wf[track] = sound.play(data, stream, wf[track])
            if play==False or track!=prev_track:
                sound.stop(stream, py_audio_handle)
                file_open = 0
            prev_track = track
                
    finally:
        sound.stop(stream, py_audio_handle)

listener =  Listener(on_press=on_press, on_release=on_release)
t = threading.Thread(target=task)

listener.start()
t.start()
try:
    listener.join()
    t.join()
finally:
    listener.stop()