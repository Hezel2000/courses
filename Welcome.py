import streamlit as st
import pandas as pd

st.subheader('Welcome')

st.write('Über die Sidebar links erhälst Du Zugriff auf derzeit 3 verfügbare online-Kurse, Kosmochemie ist in Deutsch und Englisch verfügbar.')

st.write("Zurück zu [GeoPlatform](http://www.geoplatform.de)")

st.video("https://youtu.be/WR4dNNwPejc")


# sidebar
st.sidebar.image('data_microanalysis/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")