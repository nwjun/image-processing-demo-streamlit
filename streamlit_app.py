import streamlit as st
import cv2
import numpy as np
from addNoise import noisy
import os
from filter import *

st.set_page_config(
    page_title="Image Processing",
    page_icon="📸",
    layout="centered",
    menu_items={
         'About': "# Greetings!🙋‍♀️\nHi I am a rookie who just dropped into the sea of Computer Vision recently. \
         When I started my journey, I always wish to have an insight of how each parameter affect the image, \
         and that's the reason why I started building this page! Having this website can definitely help the \
         others to get better understanding of filters and kernel in image processing as well as the concept of kernels in CNN. \
         Hope yall find it helpful! 😇"
     }
)

imagesDict = {
    "Potrait": {
        "path": "potrait.jpg",
        "credit": 'Photo by <a href="https://unsplash.com/@remik5?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Stepan Kulyk</a> on <a href="https://unsplash.com/explore?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        },
    "Street View": {
        "path": "streetView.jpg",
        "credit": 'Photo by <a href="https://unsplash.com/@samuelegiglio?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Samuele Giglio</a> on <a href="https://unsplash.com/explore?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        },
    "Girl at Beach": {
        "path": "girl-at-beach.jpg",
        "credit": 'Photo by <a href="https://unsplash.com/@iamrachelsalles?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Rachel Salles</a> on <a href="https://unsplash.com/explore?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
        },
    "Graffiti": {
    "path": "graffiti.jpg",
    "credit": 'Photo by <a href="https://unsplash.com/@robertharknessart?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Robert Harkness</a> on <a href="https://unsplash.com/s/photos/graffitti?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>',
    },
}

noiseDict = {
    'None': None,
    "Pepper": 'pepper',
    "Salt": 'salt',
    "Salt & Pepper": 's&p',
    'Gaussian': 'gaussian',
    'Poisson': 'poisson',
    'Speckle': 'speckle',
}

filterDict = {
    "Average Blur": averageBlur,
    "Median Blur": medianBlur,
    "Gaussian Blur": gaussianBlur, 
    "Canny": canny,
    "Thresholding" : threshold,
    "Bilateral Filter": bilateral,
    "Convert Colour Space": cvtColor,
}


st.title('Image Processing')
st.write("Hello peeps👋! This page is to show basic filters for image processing and how's the parameters affect the result. Feel free to try it out!")
st.write("Please share this page to your friend if you find this helpful and happy learning!")

st.markdown('### Options ⚙️')
selectedImagePath = st.selectbox("Select image", imagesDict.keys())
noise = st.selectbox("Select noise", noiseDict.keys())
option = st.selectbox("Select filter", filterDict.keys())

selectedImage = cv2.imread(os.path.join("images",imagesDict[selectedImagePath]['path']))
selectedImage = noisy(noiseDict[noise], selectedImage)

st.markdown("### Results 🪄")
st.markdown(imagesDict[selectedImagePath]['credit'], unsafe_allow_html=True)
if option != "Convert Colour Space":
    # opencv read image as BGR, have to convert to RGB
    selectedImage = cv2.cvtColor(selectedImage, cv2.COLOR_BGR2RGB)

cols = st.columns(2)
cols[0].image(selectedImage, caption="Original")
processedImg = filterDict[option](selectedImage)
cols[1].image(processedImg, caption="Processed")


st.markdown("### How's the Filter works? 💡")
showExplanation = False

showExplanation = st.checkbox("Show Explanaiton")
explanation = st.empty()

if showExplanation:
    explanation.write("Some explaination")
else:
    explanation.write("")