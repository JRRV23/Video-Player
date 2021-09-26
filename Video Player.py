#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

#Read video file
new_capture = cv2.VideoCapture('nb.mp4')

#Check if the file opened successfully
if(new_capture.isOpened()== False):
    print("Erorr for opening the video file")

#Pading the video to complete
while(new_capture.isOpened()):
    ret,frame = new_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord ('q'):
            break
    else:
        break
    
#Release when everything is completed
new_capture.realease()
cv2.destroyAllWindows() #Close all frames

