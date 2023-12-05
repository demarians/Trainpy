import requests
from rapid_api_key import x_rapidapi_key


url = "https://api-football-v1.p.rapidapi.com/v2/leagues"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': x_rapidapi_key
}
response = requests.request("GET", url, headers=headers)
print(response.text)