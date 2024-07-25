import cv2
import numpy as np
import Convert

img = cv2.imread('img/strawberry2.jpg')   # 開啟圖片
HSIImg = Convert.ToHSI(img)

cv2.imshow('RGB', img)
cv2.imshow('HSI', HSIImg)

key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destoryAllwindows()