import os
import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import convolve
from skimage import filters

#when you read an image using imread in cv2, we get a numpy array (kind of like a matrix) representing the image.
image = cv2.imread("RDJ.jpg")
#since it is a numpy array, numpy operations work on the image.

#one operation is shape, which gives you the dimension of the array.
print(image.shape)

#notice how the image has a last dimension of 3.
#this represents each color channel red, green, and blue.

#openCV has a nice function that separates the image into its color channels.
b, g, r = cv2.split(image)
#openCV has a function to show images, imshow. However, it is kind of like a stream and will close if program is no longer running.
#required args: string for name of window to display, numpy array representing image
cv2.imshow("image", image)
#instead we will use pyplot's imshow method.
#use imshow to load the image, then use show to actually display the image. 

#example:
#imshow required arguments: nparray
plt.imshow(g)
plt.show() 
plt.imshow(image)
plt.show() 

#for easier calculations, let's convert our image into a grayscale (1-dimensional) image. 

#cv2.cvtColor takes 2 required arguments: the numpy image representing image, and function for changing color space.

image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#a 1-channel image in pyplot is, by default, greenish. We can change the colormap, though!
plt.imshow(image)
plt.show()

#google the colormaps lol

plt.imshow(image, cmap="gray")
plt.show()


#pyplot uses BGR. So that's why the image seems very blue. 
#if we want a gray representation of the same image with 3 color channels, we can do this:
gray_image = np.dstack((image, image, image))
#np.dstack stacks k arrays of the same dimension (m,n) together, orming a new matrix of dimension (m,n,k)
plt.imshow(gray_image)
plt.show()

#anyways, back too manipulating the image.

#if we transpose the image, it rotates 90 degrees. the usua syntax is np.transpose(nparray), but we can also do it as follows:
image_transpose = image.T
plt.imshow(image_transpose)
plt.show()

#now fun stuff!

#we will apply a box filter to the image. 

box_filter=np.ones((10, 10))/(10*10) # define a box filter
image_boxed = convolve(image, box_filter, mode = 'same')
plt.imshow(image_boxed)
plt.show()

#other filters: 

sobel_filter = np.array([[1,0,-1], [2,0,-2],[1,0,-1]])
I_vert_edge = convolve(image, sobel_filter, mode='same')
plt.imshow(I_vert_edge)
plt.show()

sharp_filter = np.array([[0,-1,0], [-1,5,-1],[0,-1,0]])
sharp_image = convolve(image, sharp_filter, mode='same')
plt.imshow(sharp_image)
plt.show()

