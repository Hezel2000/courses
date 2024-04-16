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



@st.cache_data
def importCourseDatasheet():
    df_course_material_microanalysis = pd.read_csv('data_microanalysis/course_material_microanalysis.csv')
    df_course_material_microanalysis = df_course_material_microanalysis[df_course_material_microanalysis['ignore'] != 'yes']
    df_weekly_chapters_microanalysis = pd.read_csv('data_microanalysis/weekly chapters microanalysis.csv')
    return df_course_material_microanalysis, df_weekly_chapters_microanalysis


def useCourse(dfSearchAll, tmp):
    col1, col2 = st.columns((20,80))
    with col1:
        chapter_sel = st.radio('Kapitelauswahl', dfSearchAll['Kapitel'].drop_duplicates(), horizontal = True)
    with col2:
        dfSearchAll_tmp = dfSearchAll[dfSearchAll['Kapitel'] == chapter_sel]
        topic_sel = st.selectbox('Auswahl der Einheit', dfSearchAll_tmp['Titel'].tolist())
        sel_row = dfSearchAll.loc[dfSearchAll[dfSearchAll['Titel'] == topic_sel].index[0]]
    
    if len(sel_row) > 0:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.video(sel_row['youtube - deutsch'])
        with col2:
            st.write('Laufzeit: ' + sel_row['Laufzeit'])
            # with st.expander('Jupyter Notebooks', expanded=True):
            #     if sel_row['Lecture ipynb'] != 'none':
            #         vorlesung = "[Vorlesung](jupyter_nb/" + sel_row['Lecture ipynb'] + ")"
            #     else:
            #         vorlesung=''
            #     if sel_row['Exercise ipynb'] != 'none':
            #         uebungen = "[Übungen](jupyter_nb/" + sel_row['Exercise ipynb'] + ")"
            #     else:
            #         uebungen=''
            #     if sel_row['Solution ipynb'] != 'none':
            #         loesungen = "[Lösungen](jupyter_nb/" + sel_row['Solution ipynb'] + ")"
            #     else:
            #         loesungen=''
            #     if vorlesung=='' and uebungen=='' and loesungen=='':
            #         st.write('keine vorhanden')
            #     else:
            #         st.write(vorlesung,uebungen,loesungen)
              
            # with st.expander('Schlagworte', expanded=True):
            #     if sel_row['Schlagworte'] != 'none':
            #         st.write(sel_row['Schlagworte'])
            #     else:
            #         st.write('keine vorhanden')

        st.write(sel_row['Beschreibung'])


# import course datasheets
df_course_material_microanalysis, df_weekly_chapters_microanalysis = importCourseDatasheet()

# get date info
current_date, current_week_index, current_week_info = get_current_date(df_weekly_chapters_microanalysis)

# start webpage content
st.subheader('Willkommen zur Einführung in die Mikroanalytik')
st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')

st.divider()
display_week_content(df_weekly_chapters_microanalysis, current_week_index, current_date)
st.divider()

tab1, tab2, tab3 = st.tabs(['Lerneinheiten', 'Wochenübersicht', 'Allgemeine Informationen'])

with tab1:
    if current_week_index.tolist()[0] > 0:
        tmp = 0
        useCourse(df_course_material_microanalysis, tmp)
    else:
        tmp = 1
        useCourse(df_course_material_microanalysis, tmp)

with tab2:
    st.dataframe(df_weekly_chapters_microanalysis, width=800, hide_index=True)

with tab3:
    st.write('x')
    
#---------------------------------#
#------ Main Page Sidebar --------#
#---------------------------------#  

st.sidebar.image('data_microanalysis/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")

