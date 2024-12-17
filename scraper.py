# Importando bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/population-by-country/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table', {'id': 'example2'}).find('tbody').find_all('tr')
# print(len(rows)) checar quantidade de linhas

countries_list = []

for row in rows:
    dict = {}
    dict['Country'] = row.find_all('td')[1].text
    dict['Population (2024)'] = row.find_all('td')[2].text.replace(',','')

    countries_list.append(dict)

print(countries_list[0])

df = pd.DataFrame(countries_list)
df.to_excel('countries_data.xlsx', index=False)
df.to_csv('countries_data.csv', index=False)