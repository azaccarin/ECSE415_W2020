#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:39:32 2020

@author: AnneMarie
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
import copy

# Laplacian of Gaussian
image_path_log = "./cameraman.png" 
img_log = cv2.imread(image_path_log,cv2.IMREAD_GRAYSCALE)

#laplacian
img_lap = cv2.Laplacian(img_log, cv2.CV_32F, ksize=5)


img_edge = copy.deepcopy(img_lap)
image = copy.deepcopy(img_lap)
height,width = img_lap.shape
#print(height,width)

for i in range(0,height):
    for j in range(0,width):
        img_edge[i,j]=0
        
for i in range(1, height - 1):
        for j in range(1, width - 1):
            negative_count = 0
            positive_count = 0
            neighbour = [image[i+1, j-1],image[i+1, j],image[i+1, j+1],image[i, j-1], \
                         image[i, j+1],image[i-1, j-1],image[i-1, j],image[i-1, j+1]]
            d = max(neighbour)
            e = min(neighbour)
            for h in neighbour:
                if h>0:
                    positive_count += 1
                elif h<0:
                    negative_count += 1
 
            # If both negative and positive values exist in 
            # the pixel neighborhood, then that pixel is a 
            # potential zero crossing
            
            z_c = ((negative_count > 0) and (positive_count > 0))
            
            # Change the pixel value with the maximum neighborhood
            # difference with the pixel

            if z_c:
              if image[i,j]>0 and np.abs(e)>1500:
                  img_edge[i, j] = image[i,j] + np.abs(e)
              elif image[i,j]<0 and d>1500:
                  img_edge[i, j] = np.abs(image[i,j]) + d
            
        


img_path_canny = "./yellowlily.png"
img_canny = cv2.imread(img_path_canny)
img_canny = cv2.cvtColor(img_canny, cv2.COLOR_BGR2RGB)

I_edge = cv2.Canny(img_canny, 180, 1000, apertureSize=3)

plt.imshow(I_edge,cmap="gray")
plt.xticks([]), plt.yticks([])
plt.title('lilies')
plt.show()