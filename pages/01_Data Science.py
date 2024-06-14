#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
from utils import get_current_date, display_week_content


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


# ---------------------------------#
# ------ Vorlesungen & Übungen ----#
# ---------------------------------#


@st.cache_data
def importCourseDatasheet():
    dfSearchAll = pd.read_csv("data_science/course_material_data_science.csv")
    dfSearchAll = dfSearchAll[dfSearchAll["ignore"] != "yes"]
    df_weekly_chapters = pd.read_csv("data_science/weekly chapters data science.csv")
    return dfSearchAll, df_weekly_chapters


def useCourse(dfSearchAll, tmp):
    col1, col2 = st.columns((20, 80))
    with col1:
        # dfSearchAll
        # dfSearchAll['Kapitel'] = dfSearchAll['Kapitel'].astype(int)
        OPTIONS = dfSearchAll["Kapitel"].drop_duplicates()
        # OPTIONS = [int(_) for _ in dfSearchAll['Kapitel'].drop_duplicates()]
        if tmp == 1:
            chapter_sel = st.radio(
                "Kapitelauswahl",
                OPTIONS,
                index=current_week_index.tolist()[0],
                horizontal=True,
            )
        else:
            chapter_sel = st.radio(
                "Kapitelauswahl",
                OPTIONS,
                index=current_week_index.tolist()[0] - 1,
                horizontal=True,
            )
    with col2:
        dfSearchAll_tmp = dfSearchAll[dfSearchAll["Kapitel"] == chapter_sel]
        topic_sel = st.selectbox(
            "Auswahl der Einheit", dfSearchAll_tmp["Titel"].tolist()
        )
        sel_row = dfSearchAll.loc[
            dfSearchAll[dfSearchAll["Titel"] == topic_sel].index[0]
        ]

    if len(sel_row) > 0:
        col1, col2 = st.columns([3, 1])
        with col1:
            if isinstance(sel_row["Youtube"], str):
                # st.markdown(sel_row['Youtube'])
                st.video(sel_row["Youtube"])
        with col2:
            st.write(f'Laufzeit: {sel_row["Laufzeit"]}')
            with st.expander("Jupyter Notebooks", expanded=True):
                if sel_row["Lecture ipynb"] != "none":
                    vorlesung = (
                        f'[Vorlesung](jupyter_nb/{sel_row["Lecture ipynb"]})'
                    )
                else:
                    vorlesung = ""
                if sel_row["Exercise ipynb"] != "none":
                    uebungen = f'[Übungen](jupyter_nb/{sel_row["Exercise ipynb"]})'
                else:
                    uebungen = ""
                if sel_row["Solution ipynb"] != "none":
                    loesungen = (
                        f'[Lösungen](jupyter_nb/{sel_row["Solution ipynb"]})'
                    )
                else:
                    loesungen = ""
                if vorlesung == "" and uebungen == "" and loesungen == "":
                    st.write("keine vorhanden")
                else:
                    st.write(vorlesung, uebungen, loesungen)

            with st.expander("Schlagworte", expanded=True):
                if sel_row["Schlagworte"] != "none":
                    st.write(sel_row["Schlagworte"])
                else:
                    st.write("keine vorhanden")

        st.write(sel_row["Beschreibung"])


# ---------------------------------#
# ------ Main Page ----------------#
# ---------------------------------#

# import course datasheets
dfSearchAll, df_weekly_chapters_data_science = importCourseDatasheet()

# get date info
current_date, current_week_index, current_week_info = get_current_date(
    df_weekly_chapters_data_science
)

# Start webpage content
st.subheader("Willkommen zur Einführung in Data Sciences & Python")
st.write("*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*")

st.divider()
display_week_content(df_weekly_chapters_data_science, current_week_index, current_date)
st.divider()

tab1, tab2, tab3 = st.tabs(
    ["Lerneinheiten", "Wochenübersicht", "Allgemeine Informationen"]
)

with tab1:
    if current_week_index.tolist()[0] > 0:
        tmp = 0
        useCourse(dfSearchAll, tmp)
    else:
        tmp = 1
        useCourse(dfSearchAll, tmp)

with tab2:
    st.dataframe(df_weekly_chapters_data_science, width=800, hide_index=True)

with tab3:
    st.write(
        """**Wie zu schauen ist – oder zumindest: wie geschaut werden kann**

Anhalten, nachvollziehen, eventuell zurückspulen und dazu eigen Skizzen oder Mitschriebe anfertigen

**Die Veranstaltung besteht aus**
- ca. 100 Seiten Skript, aufgeteilt in die 3 Teilskripte
- ca. 50 Videos  mit \>7 Stunden Material
- über 100 Jupyter Notebooks  mit \>100 Fragen, Aufgaben & Beispielen
- \>100 Selbstlern-Fragen mit Antworten
- \>20 Aufgaben zur gemeinsamen Lösung in den Präsenzphasen und den Semester-Projekten
- zahlreiche zusätzlicher Dateien für verschiedene Aufgaben

Manche Videos haben aus rechtlichen Gründen ein Passwort, das gibt es separat.

**Studienleistung**
Der Kurs wird mit einer Studienleistung abgeschlosen. Dafür gibt es an den folgenden 3 Terminen:

22.05.2024, 19.06.2024, 17.07.2024

je 30 minütige Prüfungen in der letzten halben Stunde der Präsenzveranstaltung.
"""
    )

# ---------------------------------#
# ------ Main Page Sidebar --------#
# ---------------------------------#

st.sidebar.image("images/Goethe-Logo.jpg", width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")
