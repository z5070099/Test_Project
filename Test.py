import cv2
import numpy as np
import Convert

img = cv2.imread('img/strawberry2.jpg')   # 開啟圖片
img = cv2.resize(img, (400,300), interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY)
#HSIImg = Convert.ToHSI(img)

#cv2.imshow('HSI', HSIImg)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, 1, (0,255,0), 2)

cv2.imshow('RGB', img)
cv2.imshow('draw', thresh)

key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destoryAllwindows()