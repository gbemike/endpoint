import requests
import config

API_key = config.API_KEY
city_name = 'Ibadan'
limit = 5

#url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_key}'
url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}'

response = requests.get(url)
print(response.text)