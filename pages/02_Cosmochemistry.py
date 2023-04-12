import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_player import st_player
import pandas as pd

# =============================================================================
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
# =============================================================================

    
st.subheader('Willkommen zur Einführung in die Mikroanalytik')
st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')


#---------------------------------#
#------ Vorlesungen & Übungen ----#
#---------------------------------#

@st.cache_data
def import_cosmo_videos():
    return pd.read_csv('data_cosmochemistry/videos_cosmochemistry.csv')
st.session_state.cosmo_videos = import_cosmo_videos()

@st.cache_data
def import_cosmo_glossary():
    return pd.read_csv('data_cosmochemistry/glossary_cosmochemistry.csv')
st.session_state.cosmo_glossary = import_cosmo_glossary()


tab1, tab2, tab3 = st.tabs(['Videos', 'Assignments', 'Glossary'])
with tab1:
    video_sel = st.selectbox('', st.session_state.cosmo_videos['Title'])
    st.video(st.session_state.cosmo_videos[st.session_state.cosmo_videos['Title']==video_sel]['Youtube Number'].values[0])

with tab2:
    st.write('coming soon')

with tab3:
    gloss_sel = st.selectbox('', st.session_state.cosmo_glossary['Term'])
    # st.write(st.session_state.cosmo_glossary[st.session_state.cosmo_glossary['Term']==gloss_sel]['Synonym'].values[0])
    st.write(st.session_state.cosmo_glossary[st.session_state.cosmo_glossary['Term']==gloss_sel]['Explanation'].values[0])


st.sidebar.image('data_microanalysis/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")