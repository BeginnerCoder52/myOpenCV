import cv2 as cv

# Read the image from the specified path
img = cv.imread("../Photos/russian-blue-cat.jpg")  # Lùi về thư mục cha rồi vào Photos/
cv.imshow("Cat", img)

# Average Blurring
average = cv.blur(img, (3, 3))
cv.imshow("Average Blur", average)

# Gaussian Blurring
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gaussian)

# Median Blurring
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)
