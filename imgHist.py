import os
from os import listdir

from PIL import Image
import glob
import numpy as np
import math

import matplotlib.pyplot as plt
from matplotlib import colors


valDir = "./validation"
fakeDir = "./ctest10k"


def normalize(arr):
    normedArr = []
    norm = colors.Normalize(arr.min(), arr.max())
    for val in arr:
        normedArr.append(norm(val))
    return normedArr
    
#hue/sat natural
hueHistArr = []
satHistArr = []
for image in os.listdir(valDir):
    img = Image.open(valDir + "/" + image)
    hsvImg = img.convert('HSV')
    h,s,v = hsvImg.split()
    hueHist = h.histogram()
    hueHistArr.append(hueHist)
    satHist = s.histogram()
    satHistArr.append(satHist)
    print(image)
hueMean = np.mean(hueHistArr, axis = 0)
satMean = np.mean(satHistArr, axis = 0)

#hue/sat fake
hueHistArrF = []
satHistArrF = []
for image in os.listdir(fakeDir):
    img = Image.open(fakeDir + "/" + image)
    hsvImg = img.convert('HSV')
    h,s,v = hsvImg.split()
    hueHist = h.histogram()
    hueHistArrF.append(hueHist)
    satHist = s.histogram()
    satHistArrF.append(satHist)
    print(image)
hueMeanF = np.mean(hueHistArrF, axis = 0)
satMeanF = np.mean(satHistArrF, axis = 0)

#plot
plt.xlabel("bin")
plt.ylabel("normalized histogram value")

#natural hue
plt.title("Histogram distributions (hue channel, natural images)")
plt.plot(normalize(hueMean), color='k')
plt.show()

#nat sat
plt.title("Histogram distributions (saturation channel, natural images)")
plt.plot(normalize(satMean), color='k')
plt.show()

#fake hue   
plt.title("Histogram distributions (hue channel, fake images)")
plt.plot(normalize(hueMeanF), color='k')
plt.show()

#fake sat
plt.title("Histogram distributions (saturation channel, fake images)")
plt.plot(normalize(satMeanF), color='k')
plt.show()
