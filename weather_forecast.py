import requests
from bs4 import BeautifulSoup

url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XAz1Ty4zbdg'

page = requests.get(url)

# BeautifulSoup Class
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find('div', id = 'seven-day-forecast')
forecast_items = seven_day.find_all(class_ = 'tombstone-container')

def day(box): # For the present day, it show todayand not name of the day.
	day = box.find('p', class_ = "period-name").get_text()	
	return day

	
# Weather data of next week.
num = 0
for element in forecast_items:
	print("(%d) "%num + str(element) + "\n")
	num += 1

