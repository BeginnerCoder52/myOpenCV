import cv2 as cv

img = cv.imread("../Photos/cat.jpg")
cv.imshow("Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Cat", gray)

# laplacian (tiếng việt: đạo hàm bậc 2)
# Laplacian giúp chúng ta phát hiện cạnh trong ảnh.
lap = cv.Laplacian(gray, cv.CV_64F)
lap = cv.convertScaleAbs(lap)
cv.imshow("Laplacian", lap)

# Sobel (tiếng việt: đạo hàm bậc 1)
# Sobel giúp chúng ta phát hiện cạnh trong ảnh.
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow("Sobel X", sobel_x)
cv.imshow("Sobel Y", sobel_y)
cv.imshow("Combined Sobel", combined_sobel)

# Canny (tiếng việt: cạnh)
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)
cv.waitKey(0)
