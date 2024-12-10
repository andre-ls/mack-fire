import os
import json
import requests
import apache_beam as beam
from datetime import datetime, timedelta, timezone
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.pubsub import ReadFromPubSub
from apache_beam.io.gcp.bigquery import WriteToBigQuery

serviceAccount = r'cloud-714-1592328e0c49.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= serviceAccount

pipeline_options = {
    'project': 'cloud-714' ,
    'runner': 'DataflowRunner',
    'region': 'us-east1',
    'staging_location': 'gs://mack-fire/temp',
    'temp_location': 'gs://mack-fire/temp',
    'template_location': 'gs://mack-fire/template/fire_streaming',
    'save_main_session': True ,
    'streaming' : True }

pipeline_options = PipelineOptions.from_dictionary(pipeline_options)

big_query_schema = """
        'Latitude':FLOAT,
        'Longitude':FLOAT,
        'Date':DATETIME,
        'Temperature_2m':FLOAT,
        'Relative_Humidity_2m':FLOAT,
        'Apparent_Temperature':FLOAT,
        'Is_Day':INTEGER,
        'Precipitation':FLOAT,
        'Rain':FLOAT,
        'Surface_Pressure':FLOAT,
        'Wind_Speed_10m':FLOAT,
        'Wind_Direction_10m':INTEGER,
        'City':STRING,
        'State':STRING,
        'Region':STRING,
        'Country':STRING,
        'Insertion_Date':TIMESTAMP
"""

def parse_pubsub_message(message):
    return json.loads(message)

def getWeatherData(element):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={element['lat']}&longitude={element['lon']}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,surface_pressure,wind_speed_10m,wind_direction_10m")
    if response.status_code == 200:
        enrichment_data = response.json()['current']
        element.update(enrichment_data)
    return element

def getLocationData(element):
    response = requests.get(f"https://nominatim.openstreetmap.org/reverse?lat={element['lat']}&lon={element['lon']}&format=json")
    if response.status_code == 200:
        location = response.json()['address']
        filtered_location = {key: location.get(key) for key in ['municipality', 'state', 'region', 'country']}
        element.update(filtered_location)
    return element

def filterData(element):
    keys = ['lat','lon','data','temperature_2m','apparent_temperature','relative_humidity_2m','is_day','precipitation','rain','surface_pressure','wind_speed_10m','wind_direction_10m','municipality','state','region','country']
    return {k: element[k] for k in keys if k in element}

def renameFields(element):
    rename_map = {
        'lat': 'Latitude',
        'lon': 'Longitude',
        'data': 'Date',
        'temperature_2m': 'Temperature_2m',
        'relative_humidity_2m': 'Relative_Humidity_2m',
        'apparent_temperature': 'Apparent_Temperature',
        'is_day': 'Is_Day',
        'precipitation': 'Precipitation',
        'rain': 'Rain',
        'surface_pressure': 'Surface_Pressure',
        'wind_speed_10m': 'Wind_Speed_10m',
        'wind_direction_10m': 'Wind_Direction_10m',
        'municipality': 'City',
        'state': 'State',
        'region': 'Region',
        'country': 'Country'
    }
    return {rename_map.get(k, k): v for k, v in element.items()}

def addInsertionDate(element):
    utc_minus_3 = timezone(timedelta(hours=-3))
    element['Insertion_Date'] = datetime.now(utc_minus_3).isoformat()
    return element

def run():
    with beam.Pipeline(options=pipeline_options) as p:
        (p
         | 'Read from Pub/Sub' >> ReadFromPubSub(topic='projects/cloud-714/topics/fire')
         | 'Parse JSON' >> beam.Map(parse_pubsub_message)
         | 'Get Weather Data' >> beam.Map(getWeatherData)
         | 'Get Location Data' >> beam.Map(getLocationData)
         | 'Filter Fields' >> beam.Map(filterData)
         | 'Rename Fields' >> beam.Map(renameFields)
         | 'Add Insertion Date' >> beam.Map(addInsertionDate)
         | 'Write to BigQuery' >> WriteToBigQuery(
            table='cloud-714:mack_fire.fire_speed_2',
             schema=big_query_schema,
             write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
        )

if __name__ == '__main__':
    run()
