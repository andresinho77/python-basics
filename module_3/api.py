import requests


endpoint = 'http://endpoint/'
response = requests.get(endpoint)

if(response.status_code == 200):
    print(response.json())
else:
    print('Error 200')


end='http://endpoint/'
  
# location given here
location = "Netherlands"
  
# sending Post request and saving the response as response object
r = requests.post(url = end)
# extracting data in json format
data = r.json()
print(data)