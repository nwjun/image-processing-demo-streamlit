import streamlit as st
import cv2
import numpy as np

def canny(selectedImage):
    minVal = st.slider("Min Value", 0, 255, 127)
    maxVal = st.slider("Max Value", 0, 255, 255)
    apertureSize = st.slider("Aperture Size", 3, 7, step=2)
    return cv2.Canny(selectedImage, minVal, maxVal, apertureSize=apertureSize)

def threshold(selectedImage):
    threshDict = {
        "Binary": cv2.THRESH_BINARY,
        "Binary Invert": cv2.THRESH_BINARY_INV,
        "Truncate": cv2.THRESH_TRUNC,
        "Tozero": cv2.THRESH_TOZERO,
        "Tozero Invert": cv2.THRESH_TOZERO_INV
    }
    thresh = st.slider("Threshold",0, 255, 127)
    maxVal = st.slider("MaxVal", 0, 255, 255)
    threshType = st.selectbox("Threshold Type",["Binary", "Binary Invert", "Truncate", "Tozero", "Tozero Invert"])
    ret, threshImg =cv2.threshold(selectedImage,thresh, maxVal,threshDict[threshType])
    return threshImg

def averageBlur(selectedImage):
    kH = st.slider("Kernel Height", 1, 21, 5, step=2)
    kW = st.slider("Kernel Width", 1, 21, 5, step=2)
    kernel = np.ones((kW, kH), np.float32)/(kH*kW)
    return cv2.filter2D(selectedImage, -1, kernel)

def medianBlur(selectedImage):
    ksize = st.slider("Kernel Size", 3, 21, step=2)
    
    return cv2.medianBlur(selectedImage,ksize)

def gaussianBlur(selectedImage):
    kH = st.slider("Kernel Height", 1, 21, step=2)
    kW = st.slider("Kernel Width", 1, 21, step=2)
    sigmaX = st.slider("Sigma X", 0, 21)
    sigmaY = st.slider("Sigma Y", 0, 21)
    return cv2.GaussianBlur(selectedImage,(kW,kH),sigmaX=sigmaX, sigmaY=sigmaY)

def bilateral(selectedImage):
    d = st.slider("Diameter of each pixel neighbour", -1,60,5)
    sigmaColor = st.slider("Filter sigma in color space", 0 ,200,75)
    sigmaSpace = st.slider("Filter sigma in coordinate space", 0, 200,75)
    return cv2.bilateralFilter(selectedImage,d,sigmaColor, sigmaSpace)

def cvtColor(selectedImage):
    cvt = st.selectbox("Color Space", ["Grayscale", "HSV", "BGR"])
    cvtDict = {
        "Grayscale": cv2.COLOR_BGR2GRAY,
        "HSV": cv2.COLOR_BGR2HSV,
    }
    if cvt == "BGR": return selectedImage

    return cv2.cvtColor(selectedImage, cvtDict[cvt])

