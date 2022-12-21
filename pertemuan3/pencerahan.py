import cv2
import numpy as np

img = cv2.imread("../kadatua.jpg", 1);

cv2.imshow('Foto Awal',img)


cahaya =90
# [h,w] = img.shape[0:2]
[row,col] = img.shape[0:2]

# for i in np.arange(h):
#    for j in np.arange(w):
#       [r,g,b] = img[i,j]
#       b = sum(img[i,j] + cahaya)
#       if b>255:
#          b=255
#       elif b<0:
#          b=0
#       else :
#          b=b
#       img.itemset((i,j),b)
      

# a = np.zeros(img.shape)
# img[5,8] = sum(img[5, 8]+cahaya)
# print(img[5, 9])
# if img[5,8]>255:
#    img[5,8]=255
#    print(img[5, 8])

# print(sum(img[5,8]+cahaya))
for i in range(row):
   for j in range(col):
      # for s in range(len(img[i,j])):
      # else:
      #    [r,g,b]+cahaya
      # img[i,j] = img[i,j]+cahaya
      [r,g,b] = img[i,j]
      r = r+cahaya
      g = g+cahaya
      b = b+cahaya
      
      # if (img[i, j])
      if r > 255 or g > 255 or b > 255:
         r, g, b = 255,255,255
      img[i,j] = [r,g,b]
      
# for i in range(row):
#    for j in range(col):
#       img[i,j] = sum(img[i,j]*0.33)

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
      
cv2.imshow('Foto Brighnes', img);

cv2.waitKey(0);
cv2.destroyAllWindows();