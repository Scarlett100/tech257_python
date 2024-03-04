import requests,json, random
import random

# Get the list of pokemon from the API and amount of pokemon
url = 'https://pokeapi.co/api/v2/pokemon/?limit=10000'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']
print(len(pokemon_list))

# computer_random = random.sample(pokemon_list)
# print(computer_random = random.sample(pokemon_list(),[0])

#computer_random = random.choice(pokemon_list)
#print(computer_random{'name'})

#random_postcode = requests.get("https://api.postcodes.io/random/postcodes")
#print(random_postcode.json())



offset = random.randrange(1,1301)
url = 'https://pokeapi.co/api/v2/pokemon/?limit=1&offset={offset}'

response = requests.get(url)
pokemon = json.loads(response.text)['results']

pokemon_name = pokemon[0]["name"]


player1 = input("Please pick a Pokemon: ")
print(f" Thank you! your Pokemon is {player1} and the CPU pokemon is {pokemon_name }")


def














