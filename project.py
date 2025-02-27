# -*- coding: utf-8 -*-
"""project

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HdnyTc04XYrt8SLg5CsZ6sbOsPqRp-7n
"""

from google.colab import files
uploaded = files.upload()

import numpy as np
import cv2
from google.colab.patches import cv2_imshow
file_path = 'id4.webp'
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
img = cv2.imread(file_path)
if img is None:
    print("Image not loaded. Please check the file path.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for x,y,w,h in faces:
      img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
      roi_gray=gray[y:y+h,x:x+w]
      roi_color=img[y:y+h,x:x+w]
      eyes=eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
      for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2_imshow(img)

# Commented out IPython magic to ensure Python compatibility.
#using YOLO

# %pip install ultralytics
import ultralytics
ultralytics.checks()

#Run inference on an image with YOLOv8n

!yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'

#validating model using coco data set:
import torch

# Download the file
torch.hub.download_url_to_file('https://ultralytics.com/assets/coco2017val.zip', 'coco2017val.zip')

# Unzip the file and remove the zip file
!unzip -q coco2017val.zip -d datasets && rm coco2017val.zip

!yolo val model=yolov8n.pt data=coco8.yaml

"""# New Section"""