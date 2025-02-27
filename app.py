import streamlit as st
from PIL import Image

st.title("Hola mundo")

image = Image.open("julepe.jpg")

st.image(image,caption="mi imagen")



