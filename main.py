from ultralytics import YOLO
import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

model_path = os.path.join('.', 'runs', 'detect', 'train3', 'weights', 'last.pt')
model = YOLO(model_path)
vid = './validation/traffic-sign-to-test.mp4'
img = './data/images/00891.jpg'
results = model(img, show = True, verbose = True, conf = 0.2)
cv2.waitKey(0)
