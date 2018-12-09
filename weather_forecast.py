import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XAz1Ty4zbdg'

page = requests.get(url)

# BeautifulSoup Class
soup = BeautifulSoup(page.content, 'html.parser')

# Filtering data
seven_day = soup.find('div', id = 'seven-day-forecast')
forecast_items = seven_day.find_all(class_ = 'tombstone-container')

# Getting indv info
temperature = [x.get_text() for x in seven_day.select(".tombstone-container .temp")]

weather = [x.get_text() for x in seven_day.select(".tombstone-container .short-desc")]

day = [x.get_text() for x in seven_day.select(".tombstone-container .period-name")]

# Creating a dataframe
week = pd.DataFrame({'Temperature': temperature,
		     'Weather': weather}, index = day)
print(week)
