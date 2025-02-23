import cv2 as cv
import numpy as np

# Read the image from the specified path
img = cv.imread("../Photos/russian-blue-cat.jpg")  # Lùi về thư mục cha rồi vào Photos/
cv.imshow("Cat", img)

# Create a blank image with the same dimensions as the original image
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

# Split the image into its blue, green, and red components
b, g, r = cv.split(img)

# Merge the blue component with two blank channels
blue = cv.merge([b, blank, blank])
# Merge the green component with two blank channels
green = cv.merge([blank, g, blank])
# Merge the red component with two blank channels
red = cv.merge([blank, blank, r])

# Display the blue, green, and red images
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

# Print the shapes of the original and split images
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge the split components back into a single image
merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

# Wait for a key press indefinitely
cv.waitKey(0)
