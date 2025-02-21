import cv2 as cv

img = cv.imread("../Photos/cat.jpg")  # Lùi về thư mục cha rồi vào Photos/
cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Đọc Video
capture = cv.VideoCapture("../Videos/Cat_cuteness.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.5)
    cv.imshow("Video", frame)
    cv.imshow("Video", frame)
cv.waitKey(0)
