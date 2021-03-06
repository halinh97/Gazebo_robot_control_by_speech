import pyaudio
import wave
import librosa
import numpy as np
# import matplotlib.pyplot as plt


class Audio:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 2

    def createAudio(self,file_name):
        self.WAVE_OUTPUT_FILENAME =file_name
    #
        p = pyaudio.PyAudio()

        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording ****")

        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        return
if __name__ == '__main__':
    b = 1
    while b< 21:
        a=Audio()
        a.createAudio("../wav/trai%s.wav" %b)
        b = b+1
  # for i in range(1,5):
  #       x, sr = librosa.load("../wav/lui%s.wav" % i)
  #       a.createAudio("../wav/trai%s.wav" % i)
        