# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 22:51:29 2022

@author: Ahmet
"""

import cv2
import numpy as np


### 1. Video Frame Reading

# Read video from file

video_name = './Datas/3kat_kaya_ver2.avi'
cap = cv2.VideoCapture(video_name)    
i = 0

while (cap.isOpened()):
       
    # Read Images 
    ret, frame = cap.read()
    print(i)
    # Check whether readed frame is empty or not
    if np.shape(frame) == () : 
        print(' Error Empty File  ')
        break
    
    # Convert RGB to Gray
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', gray_image)
        
    # 1. Feature Detection Algorithm FAST 
    # Normally we need to use FAST-ER algorithm for speed but the python implementation is not available...
    # I take it as to do...
    
    treshold_val = 60
    
    # Initialize the tracker
    if (i == 0):
        fast = cv2.FastFeatureDetector_create(type =  2 , threshold = treshold_val)
        fast.setNonmaxSuppression(1)         # Change NonMax Suprassion Later
        
        
        
    kp = fast.detect(gray_image, None)
    kp_image = cv2.drawKeypoints(gray_image, kp, None, color=(0, 255, 0)) 
    
    # Convert the Keypoints to array points...
    pts = cv2.KeyPoint.convert(kp)
    

    # 2. Mesh Structure For Better Tracking of The Algorithm & Increasing the accuracy 
        # of the Homography Estimation
    
    
    # 3. KLT- Point Tracking Algorithm


    # 4. Homography Estimation
    
    # Rest Wıll be determined Later...

    cv2.imshow('frame', kp_image)

    if i == 0:
        break
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
    
    
    i = i + 1 # Update Frame Number

cap.release()
cv2.destroyAllWindows()

print('Finished')
