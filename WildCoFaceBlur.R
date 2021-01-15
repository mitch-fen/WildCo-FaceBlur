# WildCo faceblurring script
# Obscures human images in camera trap images
# Requires images to be run through Microsoft MegaDetector first

# M Fennell
# mitchfen@mail.ubc.ca
# Last updated: January 14, 2021

### 0. Setup workspace ####

###*** GO HERE FIRST AND DOWNLOAD MINICONDA FOR YOUR OS (this is Python + Packages) ###
### https://docs.conda.io/en/latest/miniconda.html ###

#install.packages("reticulate")
library(reticulate)

getwd() # Should be location of .Rproj, which should also contain your inputs, otherwise hard code below

### 1. Set arguments ####
json_in <- "CATH31_test.json"
img_dir_in <- "CATH31_test"
img_dir_out <- "CATH31_test_out_R"
blur_level <- 7.0
conf <- 0.3

### 2. Load in Python script ####
py_install("opencv-python", pip = TRUE) #This may take a minute your first time 
source_python("FaceBlur.py")

### 3. Execute blurring ####
face_blur(json_in,img_dir_in,img_dir_out)

# Looooooooooop

img_dirs <- list.dirs(img_dir_in) #contains imgs in site folders WITH relevant .JSON
n.sites <- len(img_dirs)
for (site in 1:len(img_dirs)){
  json_in <- 
  site_dir_out <- 
  site_dir_in <- 
  face_blur(json_in,site_dir_in,site_dir_out,blur_level,conf)
  print(paste0("Site",site,"of",len(img_dirs),"complete"))
}

