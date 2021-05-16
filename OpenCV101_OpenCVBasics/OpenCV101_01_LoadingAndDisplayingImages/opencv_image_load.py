#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday May 11 11:29:30 2021

@author: rohit
"""
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help = "path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {} pixels".format(image.shape[2]))

cv2.imshow("Image", image)
#cv2.waitkey(0)

cv2.imwrite("newimage.jpg", image)
