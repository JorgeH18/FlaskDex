from flask import Flask, request, render_template, redirect, url_for
import os, requests, requests_cache, random, datetime

app = Flask(__name__)

requests_cache.install_cache('app_cache', backend='sqlite', expire_after=300)

def get_pokemon_data(pokemon_reference):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_reference}"
    response = requests.get(url)
    pokemon_data = response.json()
    return pokemon_data

def get_pokemon_species_data(pokemon_reference):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_reference}"
    response = requests.get(url)
    pokemon_species_data = response.json()
    return pokemon_species_data

def get_latest_english_flavor_text(pokemon_species_data):
    flavor_text_entries = pokemon_species_data.get("flavor_text_entries", [])
    # Filter entries that are in English
    english_entries = [entry for entry in flavor_text_entries if entry['language']['name'] == 'en']
    # Assuming the last English entry is the latest
    latest_flavor_text = english_entries[-1]['flavor_text'].replace('\n', ' ').replace('\f', ' ')
    return latest_flavor_text

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

    # If search is done get the data from the searched pokemon
    if request.method == 'POST':
        pokemon_reference = request.form.get('pokemon_reference')
        if pokemon_reference:  # Check if search is not empty
            pokemon_data=get_pokemon_data(pokemon_reference)
            pokemon_species_data = get_pokemon_species_data(pokemon_reference)
            pokemon_flavor_text = get_latest_english_flavor_text(pokemon_species_data)
    
    return render_template('index.html', pokemon=pokemon_data, pokemon_species=pokemon_species_data, flavor_text=pokemon_flavor_text)

if __name__ == '__main__':
    app.run(debug=True)
