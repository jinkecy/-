# coding=utf-8
import pyaudio
import wave
from time import sleep
import numpy as np
def bofang():
    # define stream chunk
    chunk = 1024

    f = wave.open(r"result.wav", "rb")
    # instantiate PyAudio
    # read data
    data = f.readframes(chunk)
    try:
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        stream.write(data)
    except IOError as e :
        pass
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)
    # print data

    # paly stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()
if __name__ == '__main__':
    bofang()