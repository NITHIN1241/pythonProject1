import cv2
import winsound
cam = cv2.VideoCapture(1)
while cam. isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cytColor(diff, cv2.COLOR_RGB2GRAY)
    blur = CV2. GaussianBlur (gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, CV2. THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _= CV2.findContours(dilated, cv2.RETR_TREE, CV2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) < 5000:
           continue
        x, y, w, h = cv2.boundingRect(c)
        CV2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 6), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    if cv2.waitkey(10) == ord('q'):


        CV2.imshow('Granny Cam', frame1)