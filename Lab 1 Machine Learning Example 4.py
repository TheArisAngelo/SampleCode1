import cv2

vid = cv2.VideoCapture(0)
while (True):

    ret, frame = vid.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
