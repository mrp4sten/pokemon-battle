import random
import json


def attack(attacker, defender):
    print(f"{attacker['name']}, it's your turn. Choose an attack:")
    print("1. Basic Attack")
    print("2. Hard Attack")
    print("3. Ability")
    print("4. Block")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        attack = "basic_attack"
    elif choice == "2":
        attack = "hard_attack"
    elif choice == "3":
        attack = "ability"
    elif choice == "4":
        attack = "block"
    else:
        print("Invalid choice. Using basic attack.")
        attack = "basic_attack"

    if attack == "block":
        damage = attacker["block"]["damage"]
    else:
        damage = attacker[attack]["damage"]

    defender["health"] -= damage

    print(
        f"{attacker['name']} used {attack} on {defender['name']}. {defender['name']} has {defender['health']} health left."
    )


def get_pokemon_by_name(name, pokemons):
    for pokemon in pokemons:
        if pokemon["name"] == name:
            return pokemon
    return None


def get_team_from_file(filename, pokemons):
    with open(filename, "r") as file:
        names = file.read().splitlines()
    return [get_pokemon_by_name(name, pokemons) for name in names]


def battle():
    with open("pokemon_detils.json", "r") as file:
        pokemons = json.load(file)

    team1 = get_team_from_file("selected_pokemons.txt", pokemons)
    team2 = get_team_from_file("oponent_pokemons.txt", pokemons)

    while any(pokemon["health"] > 0 for pokemon in team1) and any(
        pokemon["health"] > 0 for pokemon in team2
    ):
        for pokemon1, pokemon2 in zip(team1, team2):
            if pokemon1["health"] > 0 and pokemon2["health"] > 0:
                attack(pokemon1, pokemon2)
                if pokemon2["health"] <= 0:
                    break
                attack(pokemon2, pokemon1)

    if any(pokemon["health"] > 0 for pokemon in team1):
        print("Team 1 wins!")
    else:
        print("Team 2 wins!")


# Start the battle
battle()
