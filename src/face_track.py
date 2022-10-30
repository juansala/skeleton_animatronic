import io
import picamera
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,160) # set Width
cap.set(4,120) # set Height

#Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/home/pi/skeleton_animatronic/xml/face_file.xml')

while True:

    ret, frame = cap.read()
    #frame = cv2.flip(frame, -1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print("Found "+str(len(faces))+" face(s)")

    if np.any(faces):
        print(str(faces[0][0]) + " " + str(faces[0][1]))

    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    #Save the result image
    #cv2.imwrite('result.jpg',image)

    #Show the result image
    #cv2.imshow("Face", frame)

    #if cv2.waitKey(1) == 27:
    #    break

cap.release()
cv2.destroyAllWindows()
