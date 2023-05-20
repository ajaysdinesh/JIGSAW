import sys
import numpy
import cv2
from scipy import datasets
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import random

image_height = 4000
image_length = 6000

image_path = sys.argv[1]
image = cv2.imread(image_path)




print(image)
pieces = []
for row in range(0,image.shape[0],500):
    for column in range(0,image.shape[1],500):
        pieces.append(image[row:row+500, column:column+500,:])

#for piece in pieces:
    #cv2.imshow('custom window',piece)
    #cv2.waitKey(0)
    #print(pieces)
# print(pieces[0])
random.shuffle(pieces)
# print(pieces[0])
big_image = image

for row in range(0,8):
    for column in range(0,12):
        cur_piece = pieces[row*12+column]  
        cur_piece.copyTo(big_image(cv2.Rect(Column*500,Row*500,cur_piece.cols,cur_piece.rows)))

cv2.namedWindow('custom window1', cv2.WINDOW_KEEPRATIO)
cv2.imshow('custom window1',image)
cv2.resizeWindow('custom window1', 1500  , 1000)
cv2.namedWindow('custom window2', cv2.WINDOW_KEEPRATIO)
cv2.imshow('custom window2',big_image)
cv2.resizeWindow('custom window2', 1500  , 1000)
cv2.waitKey(0)
cv2.destroyAllWindows()        

