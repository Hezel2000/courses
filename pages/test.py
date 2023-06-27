import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

@st.cache_data()
def load_data():
    data = pd.read_csv("./data.csv", parse_dates=["referenceDate"])
    return data

data = load_data()

shouldDisplayPivoted = st.checkbox("Pivot data on Reference Date")

gb = GridOptionsBuilder()

gb.configure_default_column(
    resizable=True,
    filterable=True,
    sortable=True,
    editable=False,
)
gb.configure_column(
    field="state", header_name="State", width=80, rowGroup=shouldDisplayPivoted
)

gb.configure_column(
    field="powerPlant",
    header_name="Power Plant",
    flex=1,
    tooltipField="powerPlant",
    rowGroup=True if shouldDisplayPivoted else False,
)
gb.configure_column(
    field="recordType",
    header_name="Record Type",
    width=110,
    rowGroup=shouldDisplayPivoted,
)

gb.configure_column(
    field="buyer",
    header_name="Buyer",
    width=150,
    tooltipField="buyer",
    rowGroup=shouldDisplayPivoted,
)

gb.configure_column(
    field="referenceDate",
    header_name="Reference Date",
    width=100,
    valueFormatter="value != undefined ? new Date(value).toLocaleString('en-US', {dateStyle:'medium'}): ''",
    pivot=False,
)

gb.configure_column(
    field="virtualYear",
    header_name="Reference Date Year",
    valueGetter="new Date(data.referenceDate).getFullYear()",
    pivot=True,
    hide=True,
)

gb.configure_column(
    field="virtualMonth",
    header_name="Reference Date Month",
    valueGetter="new Date(data.referenceDate).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",
    pivot=True,
    hide=True,
)

gb.configure_column(
    field="hoursInMonth",
    header_name="Hours in Month",
    width=50,
    type=["numericColumn"],
)
gb.configure_column(
    field="volumeMWh",
    header_name="Volume [MWh]",
    width=100,
    type=["numericColumn"],
    aggFunc="sum",
    valueFormatter="value.toLocaleString()",
)

gb.configure_grid_options(
    tooltipShowDelay=0,
    pivotMode=shouldDisplayPivoted,
)

gb.configure_grid_options(
    autoGroupColumnDef=dict(
        minWidth=300, 
        pinned="left", 
        cellRendererParams=dict(suppressCount=True)
    )
)
go = gb.build()

AgGrid(data, gridOptions=go, height=400)