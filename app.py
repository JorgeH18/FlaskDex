from flask import Flask, request, render_template, redirect, url_for
import os, requests, requests_cache, random, datetime

app = Flask(__name__)

requests_cache.install_cache('app_cache', backend='sqlite', expire_after=360)

def get_pokemon_data(pokemon_reference):
    # As names can be different (for example; giratina-altered) we get the reference from the species
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_reference}"
    response = requests.get(url)
    pokemon_data_url = response.json()["varieties"][0]["pokemon"]["url"]

    # With the pokemon reference obtained we can now get the data
    response = requests.get(pokemon_data_url)
    pokemon_data = response.json()
    return pokemon_data

def get_pokemon_species_data(pokemon_reference):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_reference}"
    response = requests.get(url)
    pokemon_species_data = response.json()
    return pokemon_species_data

def get_pokemon_ability(ability_reference):
    url = f"https://pokeapi.co/api/v2/ability/{ability_reference}"
    response = requests.get(url)
    ability_data = response.json()
    return ability_data

def get_latest_english_flavor_text(pokemon_species_data):
    flavor_text_entries = pokemon_species_data.get("flavor_text_entries", [])
    # Filter entries that are in English
    english_entries = [entry for entry in flavor_text_entries if entry['language']['name'] == 'en']
    # Assuming the last English entry is the latest
    latest_flavor_text = english_entries[-1]['flavor_text'].replace('\n', ' ').replace('\f', ' ')
    return latest_flavor_text

def get_pokemon_species_genus(pokemon_species_data):
    pokemon_species_genus = pokemon_species_data.get("genera", [])
    # Filter entries that are in English
    english_entries = [entry for entry in pokemon_species_genus if entry['language']['name'] == 'en']
    # Assuming the last English entry is the latest
    species_genus = english_entries[-1]['genus']
    return species_genus

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # Each day show a random pokemon
    today = datetime.date.today()
    random.seed(today.toordinal())
    daily_pokemon_id = random.randint(1, 1025)
    # Get data for the daily random
    pokemon_data=get_pokemon_data(daily_pokemon_id)
    pokemon_species_data = get_pokemon_species_data(daily_pokemon_id)
    pokemon_flavor_text = get_latest_english_flavor_text(pokemon_species_data)
    pokemon_species_genus = get_pokemon_species_genus(pokemon_species_data)

    # If search is done get the data from the searched pokemon
    if request.method == 'POST':
        pokemon_reference = request.form.get('pokemon_reference')
        if pokemon_reference:  # Check if search is not empty
            pokemon_data=get_pokemon_data(pokemon_reference)
            pokemon_species_data = get_pokemon_species_data(pokemon_reference)
            pokemon_flavor_text = get_latest_english_flavor_text(pokemon_species_data)
            pokemon_species_genus = get_pokemon_species_genus(pokemon_species_data)

    return render_template('index.html', pokemon=pokemon_data, pokemon_species=pokemon_species_data, flavor_text=pokemon_flavor_text, genus=pokemon_species_genus)

if __name__ == '__main__':
    app.run(debug=True)
