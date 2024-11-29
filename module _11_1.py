import requests
import pandas as pd
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

url = 'https://www.gismeteo.ru/weather-kazan-4364/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

dates = []
temperatures = []

for day in soup.find_all('div', class_='widget-row'):
    date = day.find('span', class_='widget-row__date').text.strip()
    temp = day.find('span', class_='widget-row__temp').text.strip()

    if date and temp:
        dates.append(date)
        temperatures.append(float(temp[:-1]))

weather_data = pd.DataFrame({'Date': dates, 'Temperature': temperatures})

weather_data['Date'] = pd.to_datetime(weather_data['Date'], format='%d %b')

plt.figure(figsize=(10, 5))
plt.plot(weather_data['Date'], weather_data['Temperature'], marker='o')
plt.title(f'Температура в Казане на Gismeteo')
plt.xlabel('Дата')
plt.ylabel('Температура (°C)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('gismeteo_temperature.png')
plt.show()