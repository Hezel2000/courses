import streamlit as st
# from st_aggrid import AgGrid, GridUpdateMode
# from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd

st.subheader('Welcome')

st.write('Über die Sidebar links erhälst Du Zugriff auf derzeit 3 verfügbare online-Kurse (Kosmochemie kommt in den nächsten Tagen).')

st.sidebar.image('data_microanalysis/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")