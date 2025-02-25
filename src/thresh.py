import cv2 as cv

img = cv.imread("../Photos/russian-blue-cat.jpg")
cv.imshow("Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Cat", gray)

# Simple Thresholding (tiếsng việt: ngưỡng đơn giản)
# Thresholding là một kỹ thuật xử lý ảnh cơ bản, nó được sử dụng để chuyển đổi ảnh màu sang ảnh xám.
# Thresholding giúp chúng ta chuyển đổi ảnh màu sang ảnh xám, nó giúp chúng ta chuyển đổi ảnh màu sang ảnh xám.
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholded Image", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded Inverse Image", thresh_inv)

# Adaptive Thresholding (tiếng việt: ngưỡng thích nghi)
# Adaptive Thresholding giúp chúng ta chuyển đổi ảnh màu sang ảnh xám.
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9
)
cv.imshow("Adaptive Thresholded Image", adaptive_thresh)
cv.waitKey(0)
