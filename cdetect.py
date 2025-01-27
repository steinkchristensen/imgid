import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
from tracker import *

model=YOLO('best.pt')


cap=cv2.VideoCapture('surf.mp4')


my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 


count=0
tracker=Tracker()

while True:    
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
    frame=cv2.flip(frame,1)
    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
#    print(px)
    list=[]
      
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        list.append([x1,y1,x2,y2])
        #track each object individually
    bbox_idx=tracker.update(list)
    for bbox in bbox_idx:
        x4,y4,x5,y5,id=bbox
        cv2.rectangle(frame, (x4,y4),(x5,y5),(0,255,0),2)
        cv2.putText(frame, str(id),(x5, y5), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,255),2)
   
    cv2.imshow("FRAME", frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
