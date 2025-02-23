import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../Photos/russian-blue-cat.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Mask
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)

# # Grayscale histogram (tiếng việt: biểu đồ mức xám)
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# # Tạo một biểu đồ mức xám
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Color Histogram (tiếng việt: biểu đồ màu)
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
colors = ("b", "g", "r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
