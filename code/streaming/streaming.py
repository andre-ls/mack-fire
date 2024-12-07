import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv
import json
import requests
from datetime import datetime, timedelta, timezone

# Definir opções do pipeline
class MyOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument('--input_file', type=str, help='Input CSV file to read from')
        parser.add_value_provider_argument('--output_file', type=str, help='Output CSV file to write to')

def parseCsv(line):
    headers = ['ID','Lat','Long','Satelite','Data']
    for row in csv.reader([line]):
        return dict(zip(headers, row))

def enrichData(element):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={element['Lat']}&longitude={element['Long']}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,surface_pressure,wind_speed_10m,wind_direction_10m")
    if response.status_code == 200:
        enrichment_data = response.json()['current']
        element.update(enrichment_data)
    return element

def filterData(element):
    keys = ['Lat','Long','Data','temperature_2m','apparent_temperature','relative_humidity_2m','is_day','precipitation','rain','surface_pressure','wind_speed_10m','wind_direction_10m']
    return {k: element[k] for k in keys if k in element}

def renameFields(element):
    rename_map = {
        'Lat': 'Latitude',
        'Long': 'Longitude',
        'Data': 'Date',
        'temperature_2m': 'Temperature_2m',
        'relative_humidity_2m': 'Relative_Humidity_2m',
        'apparent_temperature': 'Apparent_Temperature',
        'is_day': 'Is_Day',
        'precipitation': 'Precipitation',
        'rain': 'Rain',
        'surface_pressure': 'Surface_Pressure',
        'wind_speed_10m': 'Wind_Speed_10m',
        'wind_direction_10m': 'Wind_Direction_10m',
    }
    return {rename_map.get(k, k): v for k, v in element.items()}

def addInsertionDate(element):
    utc_minus_3 = timezone(timedelta(hours=-3))
    element['Insertion_Date'] = datetime.now(utc_minus_3).isoformat()
    return element

def run():
    options = MyOptions()
    
    with beam.Pipeline(options=options) as p:
        (p
         | 'Read from CSV' >> beam.io.ReadFromText(options.input_file, skip_header_lines=1)
         | 'Parse CSV' >> beam.Map(parseCsv)
         | 'Enrich Data' >> beam.Map(enrichData)
         | 'Filter Fields' >> beam.Map(filterData)
         | 'Rename Fields' >> beam.Map(renameFields)
         | 'Add Insertion Date' >> beam.Map(addInsertionDate)
         | 'Format to CSV' >> beam.Map(lambda x: ','.join([str(x[k]) for k in x.keys()]))
         | 'Write to CSV' >> beam.io.WriteToText(options.output_file, file_name_suffix='.csv', header='Latitude,Longitude,Date,Temperature_2m,Relative_Humidity_2m,Apparent_Temperature,Is_Day,Precipitation,Rain,Surface_Pressure,Wind_Speed_10m,Wind_Direction_10m,Insertion_Date')
        )

if __name__ == '__main__':
    run()
