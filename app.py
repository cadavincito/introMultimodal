import streamlit as st
from PIL import Image

st.title("Hola mundo")

image = Image.open("julepe.jpg")

#st.image(image,caption="mi imagen")

texto = st.text_input("escribe algo","este es mi texto")

st.write("el texto escrito es",texto)
col1, col2 = st.columns(2)

with col1:
  st.subheader("columna 1")
  st.write("las interfaces multimodales mejoran la UX")
  resp = st.checkbox("de acuerdo")
  if resp:
    st.write("correcto")

with col2:
  st.subheader("columna 1")
  modo = st.radio("que modalidad prefieres", ("visual","auditiva","tactil"))
  if modo == "visual":
    st.write("la vista es fundamental para la ui")
  if modo == "auditiva":
    st.write("la audicion es fundamental para la ui")
  if modo == "tactil":
    st.write("el tacto es fundamental para la ui")

with st.sidebar:
  st.subheader("configura la modalidad")
  
  
  
