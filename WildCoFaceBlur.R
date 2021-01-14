# WildCo faceblurring script
# Obscures human images in camera trap images
# Requires images to be run through Microsoft MegaDetector first

# M Fennell
# mitchfen@mail.ubc.ca
# Last updated: January 13, 2021

### 0. Setup workspace ####

#install.packages("reticulate")
library(reticulate)

getwd()
setwd("D:/Mitch/WildCo_FaceBlur")

### 1. Set arguments ####
json_in <- "CATH31_test.json"
img_dir_in <- "CATH31_test"
img_dir_out <- "CATH31_test_out_R"

### 2. Load in Python script ####
py_install("opencv-python", pip = TRUE)
source_python("FaceBlur.py")

face_blur(json_in,img_dir_in,img_dir_out)

