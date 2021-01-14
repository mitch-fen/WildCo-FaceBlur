# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:28:50 2021

@author: mitchfen
"""
# import the necessary packages
#import os
import numpy as np 
#pip install opencv-python
import cv2 # pip install opencv-python
import json

#os.chdir('D:\\Mitch\\WildCo_FaceBlur') # set working dir

#define faceblur function
def anonymize_face_simple(image, factor=7.0):
	# automatically determine the size of the blurring kernel based
	# on the spatial dimensions of the input image
	(h, w) = image.shape[:2]
	kW = int(w / factor)
	kH = int(h / factor)
	# ensure the width of the kernel is odd
	if kW % 2 == 0:
		kW -= 1
	# ensure the height of the kernel is odd
	if kH % 2 == 0:
		kH -= 1
	# apply a Gaussian blur to the input image using our computed
	# kernel size
	return cv2.GaussianBlur(image, (kW, kH), 0)


# Initializations (make them as arguments)
#ann_file = "D:\\Mitch\\WildCo_FaceBlur\\CATH31_test.json"
#imgs_in = "D:\\Mitch\\WildCo_FaceBlur\\CATH31_test"
#imgs_out = "D:\\Mitch\\WildCo_FaceBlur\\CATH31_test_out_0.3"

def face_blur(ann_file, imgs_in, imgs_out):
    dat = json.load(open(ann_file, "r")) # read in MD ouput .JSON
    
    print("number of images:", len(dat["images"]))
    
    for img in range(0,len(dat["images"])):
        tmp = dat["images"][img]
        file = tmp["file"]
        det = tmp["detections"]
        if len(det) != 0:
            for d in range(0,len(det)):
                tmp2 = det[d]
                bbox = tmp2["bbox"]
                cat = int(tmp2["category"])
                conf = float(tmp2["conf"])
                if cat == 2 and conf >= 0.3:
                    if d == 0:
                        image = cv2.imread(str(imgs_in)+"\\"+file)
                        (h,w) = image.shape[:2]
                        box = bbox * np.array([w, h, w, h])
                        (startX, startY, boxwide, boxhigh) = box.astype("int")
                        endX = startX + boxwide
                        endY = startY + boxhigh
                        face = image[startY:endY, startX:endX]
                        face = anonymize_face_simple(face)
                        image[startY:endY, startX:endX] = face
                        cv2.imwrite(str(imgs_out)+"\\"+file, image)
                        cv2.destroyAllWindows()
                    else:
                        image = cv2.imread(str(imgs_out)+"\\"+file)
                        (h,w) = image.shape[:2]
                        box = bbox * np.array([w, h, w, h])
                        (startX, startY, boxwide, boxhigh) = box.astype("int")
                        endX = startX + boxwide
                        endY = startY + boxhigh
                        face = image[startY:endY, startX:endX]
                        face = anonymize_face_simple(face)
                        image[startY:endY, startX:endX] = face
                        cv2.imwrite(str(imgs_out)+"\\"+file, image)
                        cv2.destroyAllWindows()
                elif cat == 2 and conf < 0.3:
                    continue
                else:
                    image = cv2.imread(str(imgs_in)+"\\"+file)
                    orig = image.copy()
                    cv2.imwrite(str(imgs_out)+"\\"+file, orig)
        else:
            image = cv2.imread(str(imgs_in)+"\\"+file)
            orig = image.copy()
            cv2.imwrite(str(imgs_out)+"\\"+file, orig)
            
            
    print("All images complete")      


