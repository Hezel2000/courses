#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from datetime import datetime
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


#---------------------------------#
#------ Vorlesungen & Übungen ----#
#---------------------------------#

@st.cache_data
def importCourseDatasheet():
    dfSearchAll= pd.read_csv('data_science/course_material_data_science.csv')
    df_weekly_chapters = pd.read_csv('data_science/weekly chapters.csv')
    return dfSearchAll, df_weekly_chapters


def useCourse(dfSearchAll):
    col1, col2 = st.columns((20,80))
    with col1:
        chapter_sel = st.radio('Kapitelauswahl', range(1,10), horizontal = True)
    with col2:
        dfSearchAll_tmp = dfSearchAll[dfSearchAll['Kapitel'] == chapter_sel]
        topic_sel = st.selectbox('Auswahl der Einheit', dfSearchAll_tmp['Titel'].tolist())
        sel_row = dfSearchAll.loc[dfSearchAll[dfSearchAll['Titel'] == topic_sel].index[0]]
    
    if len(sel_row) > 0:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.video(sel_row['Youtube'])
        with col2:
            st.write('Laufzeit: ' + sel_row['Laufzeit'])
            with st.expander('Jupyter Notebooks', expanded=True):
                if sel_row['Lecture ipynb'] != 'none':
                    vorlesung = "[Vorlesung](jupyter_nb/" + sel_row['Lecture ipynb'] + ")"
                else:
                    vorlesung=''
                if sel_row['Exercise ipynb'] != 'none':
                    uebungen = "[Übungen](jupyter_nb/" + sel_row['Exercise ipynb'] + ")"
                else:
                    uebungen=''
                if sel_row['Solution ipynb'] != 'none':
                    loesungen = "[Lösungen](jupyter_nb/" + sel_row['Solution ipynb'] + ")"
                else:
                    loesungen=''
                if vorlesung=='' and uebungen=='' and loesungen=='':
                    st.write('keine vorhanden')
                else:
                    st.write(vorlesung,uebungen,loesungen)
              
            with st.expander('Schlagworte', expanded=True):
                if sel_row['Schlagworte'] != 'none':
                    st.write(sel_row['Schlagworte'])
                else:
                    st.write('keine vorhanden')

        st.write(sel_row['Beschreibung'])
        

def display_week_content():
    df_weekly_dates = pd.DataFrame()
    df_weekly_dates['pd Datum'] = pd.to_datetime(df_weekly_chapters['Datum'])
    current_date = pd.to_datetime(datetime.now().date())
    # -----------------
    # current_date = datetime(day=16, month=5, year=2024)
    # -----------------
    current_week_index = df_weekly_dates.index[(df_weekly_dates['pd Datum'] >= current_date)]
    current_week_info = df_weekly_chapters.iloc[current_week_index.tolist()[0]]

    col1, col2 = st.columns([20,80])
    with col1:
        st.write('Überblick Woche:')
        week_nr = st.selectbox('', range(1,10), index=current_week_index.tolist()[0], label_visibility='collapsed')
        current_week_info = df_weekly_chapters.iloc[week_nr-1]
    with col2:
        st.write(f'Heute ist der: {current_date.strftime("%d.%m.%Y")}')
        with st.expander(f'bis zum: {str(current_week_info["Datum"])} –   {str(current_week_info["Thema"])}'):
            st.write('Erklärungen')


#---------------------------------#
#------ Main Page ----------------#
#---------------------------------#  
        
dfSearchAll, df_weekly_chapters = importCourseDatasheet()

st.subheader('Willkommen zur Einführung in Data Sciences & Python')
st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')

st.divider()
display_week_content()
st.divider()

tab1, tab2, tab3 = st.tabs(['Lerneinheiten', 'Wochenübersicht', 'x'])

with tab1:
    useCourse(dfSearchAll)

with tab2:
    st.dataframe(df_weekly_chapters, width=800, hide_index=True)

with tab3:
    st.write('x')


    
#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

st.sidebar.image('images/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")

