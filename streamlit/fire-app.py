import os
import numpy as np
import pandas as pd
import datetime
import bq_queries as bigquery
import altair as alt
import streamlit as st
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static
from map_config import *

st.set_page_config(layout='wide')

def setupMapSelection():
    mapView = st.radio('Tipo de Mapa',options=['Posição','Dados Metereológicos'])

    if mapView == 'Dados Metereológicos':
        measure = st.selectbox('Medida a ser exibida', options=['Temperatura','Chuva','Umidade','Vento'])
    else:
        measure = None

    return mapView, measure

def getMapConfiguration(map_view, measure):
    if map_view == 'Posição':
        return location_config
    elif map_view == 'Dados Metereológicos':
        if measure == 'Temperatura':
            return temperature_config
        if measure == 'Chuva':
            return rain_config
        if measure == 'Umidade':
            return humidity_config
        if measure == 'Vento':
            return 'Vento'

def removeUpperWhiteSpace():
    st.markdown(
        """
            <style>
                    .stAppHeader {
                        background-color: rgba(255, 255, 255, 0.0);  /* Transparent background */
                        visibility: visible;  /* Ensure the header is visible */
                    }

                   .block-container {
                        padding-top: 1rem;
                        padding-bottom: 0rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
            </style>
            """,
        unsafe_allow_html=True,
    )

def calculateCards(data):
    """
    Função responsável por calcular os valores de métricas a serem exibidos em cards na página de visualização de mapas.
    """
    totalFires = len(data)
    totalCountries = data['Country'].nunique()
    lastDate = data['Date'].max() - pd.to_timedelta(3, unit='h')

    return totalFires, totalCountries, lastDate

def positionCards(app_directory, totalFires, totalCountries, lastDate):
    space_left,\
    column_image_1, column_1,\
    column_image_2, column_2,\
    column_image_3, column_3,\
    space_right = st.columns([0.2, 0.7, 2.0, 0.7, 2.0, 0.7, 2.0, 0.2])

    with column_image_1:
        st.image(os.path.join(app_directory,"images/fire.png"),width=70)

    with column_1:
        st.metric('Total de Queimadas', totalFires)
    
    with column_image_2:
        st.image(os.path.join(app_directory,"images/globe.png"),width=70)

    with column_2:
        st.metric('Países Afetados', totalCountries)

    with column_image_3:
        st.image(os.path.join(app_directory,"images/calendar.png"),width=70)

    with column_3:
        st.metric('Última Data de Atualização', lastDate.strftime('%d/%m/%Y %H:%M'))

def generateMap(data,config):
    mapData = data.drop(['Date','Insertion_Date'],axis=1)
    map = KeplerGl(height=600, config=config)
    map.add_data(data=mapData,name='Fires')
    st.markdown('#### Mapa de Queimadas')
    keplergl_static(map)

def generateCountryBarChart(data):
    plotData = data['Country'].value_counts().sort_values(ascending=False).reset_index()
    c = alt.Chart(plotData).mark_bar().encode(y=alt.Y("Country", sort=None,title='País'), x=alt.X('count',title='Queimadas'))
    st.markdown('#### Países Afetados')
    st.altair_chart(c,use_container_width=True)

def generateScatterPlot(data):
    st.markdown('#### Condições Metereológicas')
    plotData = data[['Temperature_2m','Precipitation','Relative_Humidity_2m']]
    st.scatter_chart(plotData,x='Relative_Humidity_2m',y='Temperature_2m',x_label='Umidade',y_label='Temperatura')

removeUpperWhiteSpace()
st.title('🔥Análise de Dados de Queimadas')
with st.sidebar:
    st.title('Filtros')
    data = bigquery.getFireData()
    app_directory = os.path.dirname(__file__)
    mapView, measure = setupMapSelection()

totalFires, totalCountries, lastDate = calculateCards(data)
positionCards(app_directory, totalFires, totalCountries, lastDate)

column_left, column_right = st.columns(2)

with column_left:
    map_config = getMapConfiguration(mapView, measure)
    generateMap(data, map_config)

with column_right:
    generateCountryBarChart(data)
    removeUpperWhiteSpace()
    generateScatterPlot(data)

