import cv2
import numpy as np
cap=cv2.VideoCapture(0)
lower_range=np.array([126, 186, 47])
upper_range=np.array([179, 255, 255])
lower_range1=np.array([66, 155, 40])
upper_range1=np.array([98, 255, 255])
lower_range2=np.array([88, 176, 70])
upper_range2=np.array([133, 255, 255])

def vermemelho(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range,upper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    a=[]
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            a.append(x)
            x1=int(x+x+w)//2
            y1=int(y+y+h)//2
            cv2.circle(img,(x1,y1),4,(255,0,255),-1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(frame,("DETECT"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    p=len(a)
    cv2.putText(frame,("Vermelho:" +  str(p)),(10,432),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
def verde(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range1,upper_range1)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    b=[]
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            b.append(x)
            x2=int(x+x+w)//2
            y2=int(y+y+h)//2
            cv2.circle(img,(x2,y2),4,(255,0,255),-1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("DETECT"),(319,420),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
    p = len(b)
    cv2.putText(frame,("Verde:" + str(p)),(140,432),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
def azul(img):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_range2,upper_range2)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    d=[]
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            d.append(x)
            x3=int(x+x+w)//2
            y3=int(y+y+h)//2
            cv2.circle(img,(x3,y3),4,(255,0,255),-1)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,("DETECT"),(10,60),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    p = len(d)
    cv2.putText(frame,("Azul:" +  str(p)),(240,432),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    vermemelho(frame)
    verde(frame)
    azul(frame)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()