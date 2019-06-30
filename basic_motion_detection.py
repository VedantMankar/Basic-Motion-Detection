import cv2
import numpy

cap = cv2.VideoCapture('people.MP4')
ret,frame1 = cap.read()
ret,frame2 = cap.read()
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    #Applying gray scale
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    #Applying gaussian blur
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #Applying threshold
    _,thresh = cv2.threshold(blur,25,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    #Drawing countours
    contours , _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #Drawing rectangular shape around moving people
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        #If area less than 700 dont draw rectangle
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2,)
        cv2.putText(frame1,"Status: {}".format('movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),3)

    #cv2.drawContours(frame1,countours,-1,(0,255,0),2)

    cv2.imshow('Feed',frame1)
    frame1 = frame2
    ret,frame2 = cap.read()



    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
#cv2.release()