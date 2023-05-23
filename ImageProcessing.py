# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:01:40 2022

@author: kevin
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#import cv2

picture = mpimg.imread('battlecruiser_symbol.png')
#picture = picture[47:58, 10:20, ...]
#plt.imshow(picture)

red = picture[..., 0]
green = picture[..., 1]
blue = picture[..., 2]

convertToBlack = (red < 0.7) | (green < 0.7) | (blue < 0.7)
picture[convertToBlack] = 0
convertToWhite = (red != 0) & (green != 0) & (blue != 0)
picture[convertToWhite] = 1

#plt.imshow(picture)
#plt.imsave('battlecruiser_symbol.png', picture)

#number = picture[:, 286:292]
#plt.imshow(number)
#plt.imsave('null.png', picture)

for i in range(10):
    for j in range(4):
        picture[10, i, j] = 0

plt.imshow(picture)
plt.imsave('cruiser_symbol.png', picture)

"""
if (open("lobbyImage1.png", "rb").read() == open("unprocessedCoordinates.png", "rb").read()):
	print("True")
else:
	print("False")
"""