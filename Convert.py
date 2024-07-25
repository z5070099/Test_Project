import cv2
import numpy as np

def ToHSI(img):
    rows = int(img.shape[0])
    cols = int(img.shape[1])

    b, g, r = cv2.split(img)

    b = b/255.0
    g = g/255.0
    r = r/255.0

    HSI_img = img.copy()

    H, S, I = cv2.split(HSI_img)

    for i in range(rows):
        for j in range(cols):
            num = 0.5 * ((r[i,j] - g[i,j]) + (r[i,j] - b[i,j]))
            den = np.sqrt((r[i,j] - g[i,j]) ** 2 + (r[i,j] - b[i,j]) * (g[i,j] - b[i,j]))
            theta = float(np.arccos(num/den))

            if den == 0:
                H = 0
            elif b[i,j] <= g[i,j]:
                H = theta
            else:
                H = 2 * 3.14159265 - theta

            min_RGB = min(min(b[i,j], g[i,j]), r[i,j])
            sum = b[i,j] + g[i,j] + r[i,j]
            if sum == 0:
                S = 0
            else:
                S = 1 - 3 * min_RGB / sum
            
            H = H/(2 * 3.14159265)
            I = sum / 3.0

            HSI_img[i,j,0] = H * 255
            HSI_img[i,j,1] = S * 255
            HSI_img[i,j,2] = I * 255

    return HSI_img