import os
import datetime
import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import bq_queries as bigquery
from map_config import *
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static
from streamlit_autorefresh import st_autorefresh

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

def getLastUpdateDate(data, app_directory):
    lastDate = data['Date'].max() - pd.to_timedelta(3, unit='h')
    icon, metric = st.columns([0.2, 0.7])

    with icon:
        st.image(os.path.join(app_directory,"images/calendar_orange.png"),width=70)

    with metric:
        st.metric('Última Data de Atualização', lastDate.strftime('%d/%m/%Y %H:%M'))

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
    avgDuration = round(((data['Insertion_Date'].dt.tz_localize(None) - data['Date']).dt.total_seconds() / 60).mean())

    return totalFires, totalCountries, avgDuration

def positionCards(app_directory, totalFires, totalCountries, avgDuration):
    space_left,\
    column_image_1, column_1,\
    column_image_2, column_2,\
    column_image_3, column_3,\
    space_right = st.columns([0.2, 0.7, 2.0, 0.7, 2.0, 0.7, 2.0, 0.2])

    with column_image_1:
        st.image(os.path.join(app_directory,"images/fire_orange.png"),width=70)

    with column_1:
        st.metric('Total de Queimadas', totalFires)
    
    with column_image_2:
        st.image(os.path.join(app_directory,"images/globe_orange.png"),width=70)

    with column_2:
        st.metric('Países Afetados', totalCountries)

    with column_image_3:
        st.image(os.path.join(app_directory,"images/clock_orange.png"),width=70)

    with column_3:
        st.metric('Duração Média', f"{avgDuration} minutos")

def generateMap(data,config):
    mapData = data.drop(['Date','Insertion_Date'],axis=1)
    map = KeplerGl(height=600, config=config)
    map.add_data(data=mapData,name='Fires')
    st.markdown('#### Mapa de Queimadas')
    keplergl_static(map)

def generateCountryBarChart(data):
    plotData = data['Country'].value_counts().sort_values(ascending=False).reset_index()
    c = alt.Chart(plotData).mark_bar(color="#DF744E").encode(y=alt.Y("Country", sort=None,title='País'), x=alt.X('count',title='Queimadas'))
    st.markdown('#### Países Afetados')
    st.altair_chart(c,use_container_width=True)

def generateScatterPlot(data):
    st.markdown('#### Condições Metereológicas')
    plotData = data[['Temperature_2m','Precipitation','Relative_Humidity_2m']]
    st.scatter_chart(plotData,x='Relative_Humidity_2m',y='Temperature_2m',x_label='Umidade',y_label='Temperatura',color="#DF744E")

#Configurações da Página
removeUpperWhiteSpace()
st.title('🔥Análise de Dados de Queimadas')
with st.sidebar:
    data = bigquery.getFireData()
    app_directory = os.path.dirname(__file__)
    getLastUpdateDate(data, app_directory)
    st.title('Filtros')
    mapView, measure = setupMapSelection()
    count = st_autorefresh(interval=600000, limit=100, key="Refresher")

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

