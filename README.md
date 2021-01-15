# WildCo-FaceBlur
Obscures human identities in camera trap images after processing via Microsoft MegaDetector

## This project requires two files:
### WildCoFaceBlur.R
This script acts as a user interface and takes care of data loading, including for running multiple sites with a single call. As most camera trap users are familiar with R (and less so with Python), this script allows us to maximize the efficiency of image processing in Python, with the familiar interface of R. This script is also accesible for those with little coding experience, as there are only four inputs. 

### FaceBlur.py
This is the where the blurring process actually happens. This script takes the output from MegaDetector (a .json file), a folder of images, a confidence threshold, and a "blurriness" level, and reads the MegaDetector bounding boxes designated as humans that are above your confidence threshold, then applies a gaussian blur within that box. This script is not currently designed to be called directly within Python, and is instead called via the above R script (although it can be easily edited to do so if you're a Python user). 

## Additional Requirements
If you do not have a previous installation of Anaconda, you will need to install miniconda (a free, lightweight copy of Python, which also includes essential data science packages)

Miniconda can be downloaded here: https://docs.conda.io/en/latest/miniconda.html

## Usage


