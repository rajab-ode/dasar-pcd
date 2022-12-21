import cv2
img = cv2.imread("../kadatua.jpg")

cv2.imshow("image", img)
# cv2.imshow("image", img)

[row,column]= img.shape[0:2]

for i in range(115):
   for x in range(column):
      
      # rumusx=R.G.B * 0.33 0-255 200*0.33
      img[i,x] = sum(img[i,x])*0.33;
      
cv2.imshow("foto keabuan",img)

cv2.waitKey()
cv2.destroyAllWindows()

