import cv2 as cv

img = cv.imread("../Photos/my_class.jpg")
cv.imshow("my class", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray my class", gray)

# haar cascade (tiếng việt: tóc cascade)
# Haar cascade là một kỹ thuật phổ biến được sử dụng để nhận diện đối tượng trong ảnh hoặc video.
# Haar cascade được sử dụng để nhận diện khuôn mặt, mắt, miệng, v.v.
haar_cascade = cv.CascadeClassifier("../data/haar_face.xml")

# Detect faces (tiếng việt: phát hiện khuôn mặt)
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
print(f"Number of faces found = {len(faces_rect)}")

for x, y, w, h in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected Faces", img)
cv.waitKey(0)
