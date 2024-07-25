import cv2
img = cv2.imread('img/Car.jpg')   # 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
cv2.imshow('圖片', img)  # 使用名為 oxxostudio 的視窗開啟圖片
cv2.waitKey(0)                 # 按下任意鍵停止
cv2.destroyAllWindows() 