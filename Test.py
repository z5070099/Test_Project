import cv2
img = cv2.imread('img/Car.jpg', cv2.IMREAD_GRAYSCALE)   # 開啟圖片，預設使用 cv2.IMREAD_COLOR 模式
cv2.imwrite('./img/123.jpg', img, [cv2.IMWRITE_JPEG_QUALITY,80])