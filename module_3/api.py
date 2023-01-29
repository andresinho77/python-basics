import requests


endpoint = 'https://swapi.dev/api/planets/3/?format=json'
response = requests.get(endpoint)

if(response.status_code == 200):
    print(response.json())
else:
    print('Error 200')
