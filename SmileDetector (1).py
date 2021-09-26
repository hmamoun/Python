#!/usr/bin/env python
# coding: utf-8

# Haar Algorithm (find faces - detect smiles on faces)

# In[2]:


pip install opencv-contrib-python


# In[3]:


import cv2


# In[11]:


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
webcam = cv2.VideoCapture(0)


# In[10]:


while True:
    #read current fram from webcam
    successful_frame_read, frame = webcam.read()
    
    if not successful_frame_read:
        break
    # change to grayscale 
    frame_grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #detect faces
    faces = face_detector.detectMultiScale(frame_grayscale,1.3,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x_w,w+h),(100,200,50) , 4)
        
        #create face subimage
        face = frame[y:y+h,x:x+w]
        
        #grayscale the face
        face_grayscale = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    

