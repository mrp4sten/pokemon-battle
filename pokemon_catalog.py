import json
import os

if not os.path.exists('pokemon_detils.json'):
    with open("pokemons_full_data.json", "r") as f:
        pokemons = json.load(f)


    pokemon_details = []
    for pokemon in pokemons:
        basic_attack = (
            pokemon["moves"][0]["move"]["name"] if len(pokemon["moves"]) > 0 else "Unknown"
        )
        hard_attack = (
            pokemon["moves"][1]["move"]["name"] if len(pokemon["moves"]) > 1 else "Unknown"
        )
        pokemon_details.append(
            {
                "name": pokemon["name"],
                "experience": pokemon["base_experience"],
                "health": 100,
                "type": pokemon["types"][0]["type"]["name"],
                "basic_attack": {"name": basic_attack, "damage": 30},
                "hard_attack": {"name": hard_attack, "damage": 40},
                "ability": {
                    "name": pokemon["abilities"][0]["ability"]["name"],
                    "damage": 50,
                },
                "block": {"damage": 20},
            }
        )

    with open("pokemon_detils.json", "w") as file:
        json.dump(pokemon_details, file, indent=4)
