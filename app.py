from flask import Flask, request, render_template, redirect, url_for
import os, requests, requests_cache, random

app = Flask(__name__)

requests_cache.install_cache('app_cache', backend='sqlite', expire_after=300)

def get_pokemon_data(pokemon_reference):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_reference}"
    response = requests.get(url)
    pokemon_data = response.json()
    return pokemon_data


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pokemon_reference = request.form.get('pokemon_reference')
        #if pokemon_reference:  # Check if search is not empty
            #todo

        #return render_template('index.html', pokemon=searched_pokemon)
    random_pokemon_dex_number = random.randint(1, 1025)
    random_pokemon=get_pokemon_data("crobat")
    return render_template('index.html', pokemon=random_pokemon)

if __name__ == '__main__':
    app.run(debug=True)
