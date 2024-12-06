import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv
import json
import requests

# Definir opções do pipeline
class MyOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument('--input_file', type=str, help='Input CSV file to read from')
        parser.add_value_provider_argument('--output_file', type=str, help='Output CSV file to write to')

def parse_csv(line):
    headers = ['ID','Lat','Long','Satelite','Data']
    for row in csv.reader([line]):
        return dict(zip(headers, row))

def enrich_data(element):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={element['Lat']}&longitude={element['Long']}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,surface_pressure,wind_speed_10m,wind_direction_10m")
    if response.status_code == 200:
        enrichment_data = response.json()['current']
        element.update(enrichment_data)
    return element

def run():
    options = MyOptions()
    
    with beam.Pipeline(options=options) as p:
        (p
         | 'Read from CSV' >> beam.io.ReadFromText(options.input_file, skip_header_lines=1)
         | 'Parse CSV' >> beam.Map(parse_csv)
         | 'Enrich Data' >> beam.Map(enrich_data)
         | 'Format to CSV' >> beam.Map(lambda x: ','.join([str(x[k]) for k in x.keys()]))
         | 'Write to CSV' >> beam.io.WriteToText(options.output_file, file_name_suffix='.csv', header='ID,Lat,Long,Satelite,Data,time,interval,temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,surface_pressure,wind_speed_10m,wind_direction_10m')
         #| 'Imprimir Resultado' >> beam.Map(print)
        )

if __name__ == '__main__':
    run()
