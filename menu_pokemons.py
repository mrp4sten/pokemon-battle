import json
import pexpect
import os

with open("pokemons_full_data.json", "r") as f:
    pokemons = json.load(f)


pokemon_names = []
for pokemon in pokemons:
    pokemon_names.append(pokemon["name"])

if not os.path.exists('pokemon_names.txt'):
    with open('pokemon_names.txt', 'w') as f:
        for name in pokemon_names:
            f.write(name + '\n')



os.system('clear')

print("Select with [x] your 3 pokemons to the battle:")
command = "cat pokemon_names.txt | gum choose --height 15 --limit 3 > selected_pokemons.txt"
child = pexpect.spawn('/bin/bash', ['-c', command])
child.interact()
os.system('clear')

print("Select with [x] your 3 opponents pokemons to the battle:")
command = "cat pokemon_names.txt | gum choose --height 15 --limit 3 > oponent_pokemons.txt"
child = pexpect.spawn('/bin/bash', ['-c', command])
child.interact()
os.system('clear')


