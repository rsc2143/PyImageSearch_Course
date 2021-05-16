#!/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Thursday May 14 11:04:48 2021

@author: rohit
"""
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
                help="image to be drawn upon")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)
# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)

