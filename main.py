import subprocess

scripts = ["load_150_pokemons.py", "pokemon_catalog.py", "menu_pokemons.py", "fight_pokemons.py"]

for script in scripts:
    subprocess.run(["python", script])