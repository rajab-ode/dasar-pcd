import cv2

img = cv2.imread("../kadatua.jpg")

cv2.imshow("IMG AWAL", img)

cahaya = 90
img[1,1]+=cahaya
[row,col] = img.shape[:2]

for i in range(row):
   for j in range(col):
      
      r,g,b = img[i,j]
      r = r+cahaya
      g = g+cahaya
      b = b+cahaya
      
      if g > 255:
         g = 255
      if r > 255 :
         r= 255
      if b > 255:
         b = 255
      # if r > 255 or g > 255 or b > 255:
      #    r, g, b = 255,255,255
      
      img[i, j] = [r, g, b]
   
cv2.imshow("foto brightness", img)

cv2.waitKey(0)
cv2.destroyAllWindows()