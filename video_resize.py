import cv2


cap = cv2.VideoCapture(r"C:\Users\hm115177\Desktop\sample.mov")
# cap = cv2.VideoCapture(r"C:\Users\hm115177\Desktop\program\test.mp4")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

frame_count = int(cap.get(7))
frame_rate = int(cap.get(5))
print(frame_rate)

while cap.isOpened:
    ret, frame = cap.read()
    cv2.imshow("video", frame)

    if cv2.waitKey(int(1000/frame_rate)) == 27:
        break

cap.release()
cv2.destroyAllWindows()
