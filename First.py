from pickletools import uint8
from random import randint, random, randrange, seed
import cv2
import numpy as np

# seed(101)
img=np.zeros((250,500,3),np.uint8)

# for i in range(0,2000):
while True:    
    x=randrange(500)
    y=randrange(250)
    # x =randint(250)
    # y=randint(500)

    print(x,y)
    b=randrange(255)
    g=randrange(255)
    r=randrange(255)

    cv2.circle(img,(x,y),2,(b,g,r),-1)
    cv2.imshow("img",img)
    cv2.waitKey(10)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()    