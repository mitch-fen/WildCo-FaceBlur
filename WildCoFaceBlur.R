# WildCo faceblurring script
# Obscures human images in camera trap images
# Requires images to be run through Microsoft MegaDetector first

# M Fennell
# mitchfen@mail.ubc.ca
# Last updated: January 15, 2021

### 0. Setup workspace ####

###*** GO HERE FIRST AND DOWNLOAD MINICONDA FOR YOUR OS (this is Python + Packages) ###
### https://docs.conda.io/en/latest/miniconda.html ###

#install.packages("reticulate")
library(reticulate)

getwd() # Should be location of .Rproj, which should also contain your inputs, otherwise hard code below

### 1. Set arguments ####
img_dir_in <- "CATH_In" # Contains imgs in site folders WITH relevant .json
img_dir_out <- "CATH_Out"
blur_level <- 7.0 # Lower values of this create "blurrier" images (recommend 3-7)
conf <- 0.25 # Confidence threshold in MegaDetector output to apply blur to

### 2. Load in Python script ####
py_install("opencv-python", pip = TRUE) #This may take a minute your first time 
source_python("FaceBlur.py")

### 3. Execute blurring ####
if (dir.exists(img_dir_out) == FALSE){
  dir.create(img_dir_out)}
img_dirs <- list.dirs(img_dir_in) 
img_dirs <- img_dirs[-1]
n.sites <- length(img_dirs)

for (site in 1:length(img_dirs)){
  json_in <- list.files(img_dirs[site], pattern = "\\.json$",full.names = T)
  if (dir.exists(paste0(img_dir_out,"/", basename(img_dirs[site]))) == FALSE){
    dir.create(paste0(img_dir_out,"/", basename(img_dirs[site])))
    site_dir_out <- paste0(img_dir_out,"/", basename(img_dirs[site]))
  } else { 
  site_dir_out <- paste0(img_dir_out,"/", basename(img_dirs[site]))}
  site_dir_in <- img_dirs[site] 
  face_blur(json_in,site_dir_in,site_dir_out,blur_level,conf)
  print(paste0("Site ",site," of ",length(img_dirs)," complete"))
}

