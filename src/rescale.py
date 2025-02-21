import cv2 as cv

img = cv.imread("../Photos/cat.jpg")  # Lùi về thư mục cha rồi vào Photos/
cv.imshow("Cat", img)


def rescaleFrame(frame, scale=0.75):
    # Chỉ áp dụng cho ảnh, video, và webcam
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def changeRes(width, height):
    # Chỉ áp dụng cho Video
    capture.set(3, width)
    capture.set(4, height)
# resized_image = rescaleFrame(img)
# cv.imshow('Image_resized',resized_image)

# Đọc Video
capture = cv.VideoCapture("../Videos/Cat_cuteness.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord("d"):
        break
# cv.waitKey(0)
