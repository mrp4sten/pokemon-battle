import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=150")

pokemons_with_data = []

if response.status_code == 200:
    jsonData = response.json()
    pokemons_names = jsonData["results"]

    for pokemon in pokemons_names:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon['name']}")

        if response.status_code == 200:
            pokemon_data = response.json()
            pokemons_with_data.append(pokemon_data)
        elif response.status_code >= 400 and response.status_code < 500:
            print(f"Client error, failed to get data for {pokemon['name']}")
        elif response.status_code >= 500:
            print(f"Server error, failed to get data for {pokemon['name']}")
        else:
            print(f"Failed to get data for {pokemon['name']}")

elif response.status_code >= 404 and response.status_code < 500:
    print("Client error")
elif response.status_code >= 500:
    print("Internal server error")

with open("pokemons_full_data.json", "w") as file:
    json.dump(pokemons_with_data, file, indent=4)