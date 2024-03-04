build a CLI Pokémon Game using the Pokémon API



# Recommend using fighting game as a basis.

# Also recommend making a Pokemon lookup program first (like mine) to fully understand accessing data from an api.
T
# The Pokémon data HAS to come from the PokeApi. Main reason for this mini-project.

# Get random Pokémon for at least the CPU (Player can be chosen or random).

# Pokémon should fight and a winner should be declared in some way.

# No Pygame. Focus on interacting with the API.

# Give it your best shot! Share your code at COB (17:00)

# Starter code:

import requests
import json

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

# Ask the user to choose a pokemon
print('Enter your pokemon:')
# for pokemon in pokemon_list:
    # print(pokemon['name'])

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(pokemon_data['height'])
weight = int(pokemon_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(pokemon_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))