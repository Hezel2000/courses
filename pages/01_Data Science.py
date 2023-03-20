#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
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

    
st.subheader('Willkommen zur Einführung in Data Sciences')
st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')

#---------------------------------#
#------ Vorlesungen & Übungen ----#
#---------------------------------#
#def Vorlesungen_Uebungen():
import streamlit as st
st.subheader('Wähle Deine Lerneinheit')

@st.cache
def importCourseDatasheet():
    dfSearchAll= pd.read_csv('https://raw.githubusercontent.com/Hezel2000/Data_Science/main/course_material_data_science.csv')
    return dfSearchAll


def useCourse(dfSearchAll):
    dfSearchAll = dfSearchAll
    gd = GridOptionsBuilder.from_dataframe(dfSearchAll)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(editable=True,groupable=True)
    gd.configure_selection(selection_mode='single', use_checkbox=True)
    gridoptions = gd.build()
    grid_table = AgGrid(dfSearchAll, gridOptions=gridoptions, update_mode = GridUpdateMode.SELECTION_CHANGED, theme='material')
    sel_row = grid_table['selected_rows']

    if len(sel_row) > 0:    
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.video(sel_row[0]['Youtube'])
        with col2:
            st.write('Laufzeit: ' + sel_row[0]['Laufzeit'])
            with st.expander('Jupyter Notebooks', expanded=True):
                if sel_row[0]['Vorlesung ipynb'] != 'none':
                    vorlesung = "[Vorlesung](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Vorlesung ipynb'] + ")"
                else:
                    vorlesung=''
                if sel_row[0]['Übungen ipynb'] != 'none':
                    uebungen = "[Übungen](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Übungen ipynb'] + ")"
                else:
                    uebungen=''
                if sel_row[0]['Lösungen ipynb'] != 'none':
                    loesungen = "[Lösungen](https://raw.githubusercontent.com/Hezel2000/Data_Science/main/jupyter_nb/" + sel_row[0]['Lösungen ipynb'] + ")"
                else:
                    loesungen=''
                if vorlesung=='' and uebungen=='' and loesungen=='':
                    st.write('keine vorhanden')
                else:
                    st.write(vorlesung,uebungen,loesungen)
            with st.expander('Schlagworte', expanded=True):
                if sel_row[0]['Schlagworte'] != 'none':
                    st.write(sel_row[0]['Schlagworte'])
                else:
                    st.write('keine vorhannden')
        
        #st.subheader('Beschreibung')
        st.write(sel_row[0]['Beschreibung'])

# =============================================================================
#         else:
#             st.subheader('Wähle eine Einheit aus obiger Liste')
# =============================================================================
        

dfSearchAll = importCourseDatasheet()

useCourse(dfSearchAll)


    
#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

# st.sidebar.image('../images/Goethe-Logo.jpg', width=150)

st.sidebar.write("Viele Wege führen zum Erfolg.")

