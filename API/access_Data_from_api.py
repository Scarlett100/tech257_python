import requests, json

# Get the list of pokemon from the api

# store url in a variable

url = "https://"
response = requests.get(url)
pokemon_list = json.loads(response.text)["results"]
print(pokemon_list)

# Ask user to choose a pokemon
print("Enter")



