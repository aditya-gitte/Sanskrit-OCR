import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Images/1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def thresholding(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY_INV)
    # plt.imshow(thresh, cmap='gray')
    return thresh

thresh_img = thresholding(img);

#dilation
kernel = np.ones((3,85), np.uint8)
dilated = cv2.dilate(thresh_img, kernel, iterations = 1)
plt.imshow(dilated, cmap='gray');

(contours, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
sorted_contours_lines = sorted(contours, key = lambda ctr : cv2.boundingRect(ctr)[1]) # (x, y, w, h)

img2 = img.copy()

for ctr in sorted_contours_lines:
    x, y, w, h = cv2.boundingRect(ctr)
    cv2.rectangle(img2, (x, y), (x + w, y + h), (40, 100, 250), 2)

# plt.imshow(img2);


# Display result
cv2.imshow('Result', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
