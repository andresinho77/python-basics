import requests


endpoint = 'http://castlemock-env.eba-ashcqwxv.us-east-1.elasticbeanstalk.com/mock/rest/project/iOR4Js/application/tehwi6/'
response = requests.get(endpoint)

if(response.status_code == 200):
    print(response.json())
else:
    print('Error 200')


end='http://castlemock-env.eba-ashcqwxv.us-east-1.elasticbeanstalk.com/mock/rest/project/iOR4Js/application/tehwi6/'
  
# location given here
location = "Netherlands"
  
# sending Post request and saving the response as response object
r = requests.post(url = end)
# extracting data in json format
data = r.json()
print(data)