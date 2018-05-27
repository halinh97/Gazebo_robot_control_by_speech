import CreateAudio

import librosa
import numpy as np

def chooseAction():
    arr = []
    for i in range(1,10):
        x, sr = librosa.load("../wav/trai%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)

    for i in range(1,10):
        x, sr = librosa.load("../wav/phai%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)

    for i in range(1,10):
        x, sr = librosa.load("../wav/tien%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)

    for i in range(1,10):
        x, sr = librosa.load("../wav/lui%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)
   
    while True:
        test = CreateAudio.Audio()
        test.createAudio("../wav/test.wav")
        x, sr = librosa.load("../wav/test.wav")
        mfcc = librosa.feature.mfcc(x, sr)
        delta = []
        for i in range(len(arr)):
            delta.append(np.linalg.norm(mfcc - arr[i]))
        min1 = min(delta)
        # print(delta)
        # print(min1)
        print((delta.index(min1))/10)
        if ((delta.index(min1))/10) == 0 :
            print("*** TRAI ****")
        if ((delta.index(min1))/10) == 1 :
            print("*** PHAI ****")
        if ((delta.index(min1))/10) == 2 :
            print("*** TIEN ****")
        if ((delta.index(min1))/10) == 3 :
            print("*** LUI ****")
        return (delta.index(min1))/10

def Action():
    return chooseAction()
        
