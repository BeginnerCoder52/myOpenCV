import cv2 as cv
import numpy as np

img = cv.imread("../Photos/cat.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# Create a circle mask (tiếng việt: tạo mặt nạ hình tròn)
# mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
# cv.imshow("Mask", mask)

circle = cv.circle(
    blank.copy(), (img.shape[1] // 2 + 45, img.shape[0] // 2), 100, 255, -1
)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("Weird Shape", weird_shape)

# Mask the image (tiếng việt: che mặt)
masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("Masked Image", masked)

cv.waitKey(0)
