import CreateAudio
import librosa
import numpy as np
from scipy.spatial.distance import euclidean


from fastdtw import fastdtw


def chooseAction():
    arr = []
    for i in range(1,31):
        x, sr = librosa.load("../wav1/trai%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)
    for i in range(1,31):
        x, sr = librosa.load("../wav1/phai%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)

    for i in range(1,31):
        x, sr = librosa.load("../wav1/tien%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)

    for i in range(1,31):
        x, sr = librosa.load("../wav1/lui%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)
    return arr
def Action(arr):
    test = CreateAudio.Audio()
    test.createAudio("../test/test.wav")
    x, sr = librosa.load("../test/test.wav")
    mfcc = librosa.feature.mfcc(x, sr)

    delta = []
    print len(arr)
    for i in range(len(arr)):
        distance, path = fastdtw(mfcc, arr[i], dist=euclidean)
        delta.append(distance)

    mins = min(delta)
    # min1 = min(delta1)
    index = (delta.index(mins))/30
    print(index)
    if index == 0 :
        print("*** TRAI ****")
    if index == 1 :
        print("*** PHAI ****")
    if index == 2 :
        print("*** TIEN ****")
    if index == 3 :
        print("*** LUI ****")
    return (index)
arr = chooseAction()
# Action(arr)
# arr = Action()
# a = 1
# while a < 6:
    # Action(arr)
    # a = a + 1
