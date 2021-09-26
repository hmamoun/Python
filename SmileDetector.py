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




