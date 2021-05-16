#!/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Wednesday May 14 12:24:42 2021

@author: rohit
"""

import cv2
import cv2.cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype = "uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0,0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 10)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 255), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (150, 0, 0)
cv2.rectangle(canvas, (100, 100), (200, 200), blue, -5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300,300,3), dtype = "uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
