import numpy as np
import cv2 as cv
fileURL = "video.mp4"
cap = cv.VideoCapture(fileURL)

#Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

while True:
    #Capture frame-by-frame
    ret, frame = cap.read()
    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive video frame (stream end?). Exiting...")
        break
    frame = cv.resize(frame, (640, 480))
    out.write(frame)
    #Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

#When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()