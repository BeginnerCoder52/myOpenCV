import cv2 as cv

# img = cv.imread("../Photos/cat.jpg")  # Lùi về thư mục cha rồi vào Photos/

# if img is None:
#     print("Error: Cannot load image. Check file path!")
# else:
#     cv.imshow("Cat", img)
#     cv.waitKey(0)

capture = cv.VideoCapture("../Videos/Cat_cuteness.mp4")

while True:
    isTrue, frame = capture.read()
    if not isTrue:  # Nếu không còn frame nào, thoát vòng lặp
        break

    cv.imshow("Video", frame)

    # Kiểm tra nếu cửa sổ bị đóng
    if cv.getWindowProperty("Video", cv.WND_PROP_VISIBLE) < 1:
        break

    # Nếu nhấn phím 'd', thoát vòng lặp
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

# Giải phóng tài nguyên
capture.release()
cv.destroyAllWindows()
