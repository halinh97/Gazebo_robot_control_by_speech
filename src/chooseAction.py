import CreateAudio

import librosa
import numpy as np


def chooseAction():

    codebook = []
    avg = []
    for i in range(1,11):
            x, sr = librosa.load("../wav/trai%s.wav" %i)
            mfcc = librosa.feature.mfcc(x,sr)
            avg.append(mfcc)


    codebook.append(sum(avg)/float(len(avg)))
    avg = []
    for i in range(1,11):
            x, sr = librosa.load("../wav/phai%s.wav" % i)
            mfcc = librosa.feature.mfcc(x, sr)

            avg.append(mfcc)
    codebook.append(sum(avg) / float(len(avg)))

    avg = []
    for i in range(1,11):
            x, sr = librosa.load("../wav/tien%s.wav" % i)
            mfcc = librosa.feature.mfcc(x, sr)

            avg.append(mfcc)
    codebook.append(sum(avg) / float(len(avg)))

    avg = []
    for i in range(1,11):
            x, sr = librosa.load("../wav/lui%s.wav" % i)
            mfcc = librosa.feature.mfcc(x, sr)
            avg.append(mfcc)
    codebook.append(sum(avg) / float(len(avg)))


    test = CreateAudio.Audio()
    test.createAudio("../wav/test.wav")
    x,sr = librosa.load("../wav/test.wav")
    mfcc = librosa.feature.mfcc(x,sr)
    delta = []
    for i in range(4):
        delta.append(mfcc-codebook[i])

    do_dai=[]

    for i in range(4):
        do_dai.append(np.linalg.norm(delta[i]))
    print(do_dai,"111111444444")
    value = min(do_dai)
    return do_dai.index(value)


if __name__ == '__main__':
    print(chooseAction())


