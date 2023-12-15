import requests

API_KEY = '572a4a00b09116a37b3062ea0313caa3'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input ("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data ['weather'][0]['description']
    temperature = round(data ['main']['temp']-273.15,2)
    print("Clima:", weather)
    print("Temperatura:", temperature, "celsius")
else:
    print('An error occurred!')
