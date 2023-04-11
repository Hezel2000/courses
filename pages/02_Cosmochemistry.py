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

st.subheader('Wähle Deine Lerneinheit')

@st.cache
def importCourseDatasheet():
    dfSearchAll= pd.read_csv('data_cosmochemistry/course_material_microanalysis.csv')
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
            if sel_row[0]['youtube - deutsch'] != 'vim':
                st.video(sel_row[0]['youtube - deutsch'])
            else:
                st_player(sel_row[0]['vimeo'])
        with col2:
            st.write('Laufzeit: ' + sel_row[0]['Laufzeit'])
            with st.expander('Schlagworte', expanded=True):
                if sel_row[0]['Schlagworte'] != 'none':
                    st.write(sel_row[0]['Schlagworte'])
                else:
                    st.write('keine vorhannden')
        
        #st.subheader('Beschreibung')
        st.write(sel_row[0]['Beschreibung'])


dfSearchAll = importCourseDatasheet()
useCourse(dfSearchAll)

st.sidebar.image('data_microanalysis/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")