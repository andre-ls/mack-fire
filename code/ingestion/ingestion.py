import os
import json
import requests
import pandas as pd
import functions_framework
from bs4 import BeautifulSoup
from google.cloud import pubsub_v1

def getHtmlTable():
    url = 'https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/10min/'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', class_='table')

    if not table:
        print("Tabela não encontrada.")
    else:
        headers = [cell.get_text(strip=True) for cell in table.find('div', class_='row header').find_all('div', class_='cell')]

        rows = table.find_all('div', class_='row')[1:]
        data = [[cell.get_text(strip=True) for cell in row.find_all('div', class_='cell')] for row in rows]
        df = pd.DataFrame(data, columns=headers)

        return df

def getMostRecentFileName(table):
    table['Última modificação'] = pd.to_datetime(table['Última modificação'], format='%d/%m/%Y %H:%M:%S')
    mostRecentDate = table['Última modificação'].max()
    mostRecentFileName = table[table['Última modificação'] == mostRecentDate]['Nome'].iloc[0]
    return mostRecentFileName

def requestData(fileName):
    url = f'https://dataserver-coids.inpe.br/queimadas/queimadas/focos/csv/10min/{fileName}'
    data = pd.read_csv(url)
    return data

def generateJson(data):
    return data.to_json(orient='records')

def sendMessage(google_project, pubsub_topic, json_data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(google_project, pubsub_topic)

    for row in json.loads(json_data):
        message = json.dumps(row)
        future = publisher.publish(topic_path, message.encode('utf-8'))
        print(f'Publicando mensagem: {message}')
        print(f'Publicada com ID: {future.result()}')
        print('-'*100)

def runIngestion():
    google_project = 'cloud-714'
    pubsub_topic = 'fire'

    fileTable = getHtmlTable()
    fileName = getMostRecentFileName(fileTable)
    data = requestData(fileName)
    json_data = generateJson(data)
    sendMessage(google_project, pubsub_topic, json_data)

@functions_framework.http
def cloudEntrypoint(request):
    runIngestion()
    return 'OK'

if __name__ == '__main__':
    runIngestion()

