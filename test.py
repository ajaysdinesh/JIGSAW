import sys
import numpy
import cv2
from scipy import datasets
import imageio.v2 as imageio
import matplotlib.pyplot as plt

image_path = sys.argv[1]
image = cv2.imread(image_path)
cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
cv2.imshow('custom window', image)
cv2.resizeWindow('custom window', 1500  , 1000)


for r in range(0,image.shape[0],500):
    for c in range(0,image.shape[1],500):
        cv2.imwrite(f"img{r}_{c}.png",image[r:r+500, c:c+500,:])

cv2.waitKey(0)
cv2.destroyAllWindows()        

