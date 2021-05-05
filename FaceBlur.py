# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:28:50 2021

Blurs camera trap images identified as human by Microsoft MegaDetector

M Fennell
mitchfen@mail.ubc.ca

@author: mitchfen
"""
# import the necessary packages
import numpy as np 
#pip install opencv-python
import cv2 
import json
import os

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


# Initializations 

def face_blur(ann_file, imgs_in, imgs_out, blur, conf_lim):
    dat = json.load(open(ann_file, "r")) # read in MD ouput .JSON
        
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
                if cat == 2 and conf >= conf_lim:
                    if d == 0:
                        image = cv2.imread(str(imgs_in)+"\\"+file)
                        (h,w) = image.shape[:2]
                        box = bbox * np.array([w, h, w, h])
                        (startX, startY, boxwide, boxhigh) = box.astype("int")
                        endX = startX + boxwide
                        endY = startY + boxhigh
                        face = image[startY:endY, startX:endX]
                        face = anonymize_face_simple(face, factor=blur)
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
                        face = anonymize_face_simple(face, factor=blur)
                        image[startY:endY, startX:endX] = face
                        cv2.imwrite(str(imgs_out)+"\\"+file, image)
                        cv2.destroyAllWindows()
                else:
                    image = cv2.imread(str(imgs_in)+"\\"+file)
                    orig = image.copy()
                    cv2.imwrite(str(imgs_out)+"\\"+file, orig)
        else:
            image = cv2.imread(str(imgs_in)+"\\"+file)
            orig = image.copy()
            cv2.imwrite(str(imgs_out)+"\\"+file, orig)
            
    print("All",len(dat["images"]),"images at site",os.path.basename(imgs_out),"complete")      
    dat.clear()

