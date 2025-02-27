import streamlit as st
from PIL import Image

st.title("Hola mundo")

image = Image.open("julepe.jpg")

#st.image(image,caption="mi imagen")

texto = st.text_input("escribe algo","este es mi texto")

st.write("el texto escrito es",texto)

