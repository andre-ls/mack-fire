import requests
import pandas as pd
from bs4 import BeautifulSoup

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

if __name__ == '__main__':
    fileTable = getHtmlTable()
    fileName = getMostRecentFileName(fileTable)
    data = requestData(fileName)
    data.to_csv(f'./data/ingestion/{fileName}.csv')
