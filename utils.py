import streamlit as st
import pandas as pd
from datetime import datetime


def display_week_content(df_weekly_chapters_data_science, current_week_index, current_date):
    df_weekly_chapters = df_weekly_chapters_data_science
    col1, col2 = st.columns([20,80])
    with col1:
        st.write('Überblick Woche:')
        week_nr = st.selectbox('', df_weekly_chapters['Woche'], index=current_week_index.tolist()[0], label_visibility='collapsed')
        current_week_info = df_weekly_chapters.iloc[week_nr]
    with col2:
        st.write(f'Heute ist der: {current_date.strftime("%d.%m.%Y")}')
        with st.expander(f'bis zum: {str(current_week_info["Datum"])} –   {str(current_week_info["Thema"])} – Gesamtlaufzeit: {str(current_week_info["Laufzeit"])}', expanded=True):
            st.write(current_week_info["Beschreibung"])


# Get current dat info
def get_current_date(df_weekly_chapters_data_science):
    df_weekly_chapters = df_weekly_chapters_data_science
    df_weekly_dates = pd.DataFrame()
    df_weekly_dates['pd Datum'] = pd.to_datetime(df_weekly_chapters['Datum'])
    # current_date = pd.to_datetime(datetime.now().date())
    current_date = datetime(day=13, month=4, year=2024)
    current_week_index = df_weekly_dates.index[(df_weekly_dates['pd Datum'] >= current_date)]
    current_week_info = df_weekly_chapters.iloc[current_week_index.tolist()[0]]
    return current_date, current_week_index, current_week_info