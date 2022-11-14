import cv2

cap = cv2.VideoCapture(0)


def __open__webcam():
    while True:
        ret, frame = cap.read()

        cv2.imshow('webcam feed', frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break

    cap.release()
    cv2.destroyAllWindows()