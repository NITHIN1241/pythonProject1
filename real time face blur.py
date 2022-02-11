# import the necessary packages
import cv2

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier( "haarcascade_frontalface_default.xml')

while True:
    success, img = cap.read()
    faces faceCascade.detectMultiscale( img, 1.2,4)
    for (x, y, w, h) in faces:
    # To make a face blurred
    ROI = img[y:y+h, X:X+w]
    blur = cv2.Gaussianblur(ROI, (91,91), )
    # Insert ROI back into image
    img[y:y+h, X:X+w] = blur
    # To make a bounding box #*(Not Necessary)
    # cv2.rectangle( img, (x,y), (x+w, y+h), (0,255,0),4).
if faces==():
    CV2.putText( img, 'No Face Found!', (20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
CV2.imshow( 'Face Blur', img)
if cv2.waitKey(1) & Oxff==ord('q'):
    break
# Turn camera off
cap.release)
# Close camera window
CV2.destroyAllWindows