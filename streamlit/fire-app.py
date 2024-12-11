import os
import numpy as np
import pandas as pd
import bq_queries as bigquery
import streamlit as st
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static

st.set_page_config(layout='wide')

def setupMapSelection():
    map_view = st.radio('Tipo de Mapa',options=['Posição','Dados Metereológicos'])

    if map_view == 'Dados Metereológicos':
        measure = st.selectbox('Medida a ser exibida', options=['Temperatura','Precipitação','Umidade','Vento'])
    else:
        measure = None

def getMapConfiguration(map_view, measure):
    if map_view == 'Posição':
        return tracks_config
    elif map_view == 'Dados Metereológicos':
        if measure == 'Temperatura':
            return 'Temperatura'
        if measure == 'Precipitação':
            return 'Precipitação'
        if measure == 'Umidade':
            return 'Umidade'
        if measure == 'Vento':
            return 'Vento'

def calculateCards(data):
    """
    Função responsável por calcular os valores de métricas a serem exibidos em cards na página de visualização de mapas.
    """
    totalFires = len(data)
    totalCountries = data['Country'].nunique()
    lastDate = data['Date'].max()

    return totalFires, totalCountries, lastDate

def positionCards(app_directory, totalFires, totalCountries, lastDate):
    space_left,\
    column_image_1, column_1,\
    column_image_2, column_2,\
    column_image_3, column_3,\
    space_right = st.columns([1.0, 0.7, 2.0, 0.7, 2.0, 0.7, 2.0, 0.2])

    with column_image_1:
        st.image(os.path.join(app_directory,"images/fire.jpeg"),width=70)

    with column_1:
        st.metric('Total de Queimadas', totalFires)
    
    with column_image_2:
        st.image(os.path.join(app_directory,"images/globe.jpeg"),width=70)

    with column_2:
        st.metric('Países Afetados', totalCountries)

    with column_image_3:
        st.image(os.path.join(app_directory,"images/calendar.jpeg"),width=70)

    with column_3:
        st.metric('Última Data de Atualização', lastDate)

def generateMap(data, map_config):
    map = KeplerGl(height=600, config=map_config)
    map.add_data(data=mapData,name='Fires')
    keplergl_static(map,width=1250)

st.title('🔥Análise de Dados de Queimadas')
with st.sidebar:
    st.title('Filtros')
    data = bigquery.getFireData()
    app_directory = os.path.dirname(__file__)

totalFires, totalCountries, lastDate = calculateCards(data)
positionCards(app_directory, totalFires, totalCountries, lastDate)
map_config = getMapConfiguration(map_view, measure)
generateMap(data, map_config)

