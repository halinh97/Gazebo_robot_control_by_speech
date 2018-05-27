import CreateAudio
import librosa
import numpy as np
from scipy.spatial.distance import euclidean
# from dtw import dtw
# from numpy.linalg import norm

from fastdtw import fastdtw


def chooseAction():
    arr = []
    for i in range(1,21):
        x, sr = librosa.load("../wav1/trai%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)
    for i in range(1,21):
        x, sr = librosa.load("../wav1/phai%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)

    for i in range(1,21):
        x, sr = librosa.load("../wav1/tien%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)

    for i in range(1,21):
        x, sr = librosa.load("../wav1/lui%s.wav" % i)
        mfcc = librosa.feature.mfcc(x, sr)
        arr.append(mfcc)
    a = 1
    while a < 6:
        test = CreateAudio.Audio()
        test.createAudio("../testwav/test%s.wav" %a)
        x, sr = librosa.load("../testwav/test%s.wav" %a)
        mfcc = librosa.feature.mfcc(x, sr)

        delta = []
        print len(arr)
        for i in range(len(arr)):
            distance, path = fastdtw(mfcc, arr[i], dist=euclidean)
            delta.append(distance)

            # dist, cost, acc_cost, path = dtw(mfcc.T, arr[i].T, dist=lambda x, y: norm(x - y, ord=1))
            # delta1.append(dist)
        mins = min(delta)
        # min1 = min(delta1)
        index = (delta.index(mins))/19
        # index1 = (delta1.index(min1))/19
        print(index)
        # print(index1)
        if index == 0 :
            print("*** TRAI ****")
        if index == 1 :
            print("*** PHAI ****")
        if index == 2 :
            print("*** TIEN ****")
        if index == 3 :
            print("*** LUI ****")
        a = a + 1
        # return (index)
    
chooseAction()