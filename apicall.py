import requests
import json

url = 'https://pokeapi.co/api/v2/region/'  # Replace with the actual API URL
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

json_formatted_str = json.dumps(data, indent=7)

with open("output.txt","w") as file:
    file.write(json_formatted_str)