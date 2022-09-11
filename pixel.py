from turtle import color
from webbrowser import get
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("check.png")

cv2.imshow("image",img)
img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


any_pxl= img[0,0]
print(any_pxl)

in_img= img[0:,0:]
print(in_img)
cv2.imshow("in_img",in_img)

plt.xticks([])
plt.yticks([])
plt.imshow(in_img)
plt.show()

cv2.waitKey(0)