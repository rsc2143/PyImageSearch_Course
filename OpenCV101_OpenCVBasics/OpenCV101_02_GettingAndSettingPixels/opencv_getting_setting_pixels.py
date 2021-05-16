#!/usr/bin/env python3
# -*- coding utf-8 -*-
"""
Created on Wednesday May 12 7:51:31 2021

@author: rohit
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
                help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("pixel at [0, 0] - Red - {}, Green - {}, Blue - {}".format(r, g, b))

(b, g, r) = image[20, 50]
print("pixel at [20, 50] - Red - {}, Green - {}, Blue - {}".format(r, g, b))

image[20, 50] = (0, 0, 255)
(b, g, r) = image[20, 50]
print("pixel at [20, 50] - Red - {}, Green - {}, Blue - {}".format(r, g, b))

(cX, cY) = (w // 2, h // 2)

tl = image[0:cY, 0:cX]
cv2.imshow("Top-left corner", tl)

tr = image[0:cY, cX:w]
cv2.imshow("Top-right corner", tl)

bl = image[cY:h, 0:cX]
cv2.imshow("Bottom-left corner", bl)

br = image[cY:h, cX:w]
cv2.imshow("Bottom-right corner", br)

image[0:cY, 0:cX] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)

