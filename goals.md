
# Challenge: Simple Pokemon Information Application

**Description:**

Build a Flask application that fetches and displays Pokemon information from the PokeAPI (pokeapi.co). The application should:

1.  **Allow users to search for a Pokemon:** Provide a form for users to input a Pokemon name or ID.
2.  **Fetch Pokemon data from the API:** Use the PokeAPI to retrieve Pokemon data based on the search term.
3.  **Display the Pokemon information:** Display relevant Pokemon information, such as the Pokemon's name, image, types, abilities, and stats.

**Milestones:**

1.  **Basic Search and Display:**
    * Implement a form for users to enter a Pokemon name or ID.
    * Fetch the Pokemon data from the PokeAPI based on the search term.
    * Display the Pokemon's name and image.
2.  **Display Additional Information:**
    * Display the Pokemon's types and abilities.
3.  **Display Pokemon Stats:**
    * Display the Pokemon's base stats (HP, Attack, Defense, Special Attack, Special Defense, Speed).
4.  **Error Handling:**
    * Handle potential errors, such as:
        * Pokemon not found.
        * API errors.
        * Invalid input.
5.  **Styling and User Interface:**
    * Implement basic CSS styling to make the application visually appealing.
    * Ensure the user interface is easy to use and understand.

**Technical Requirements:**

* Use Flask for the web framework.
* Use Jinja2 for templating.
* Use the `requests` library to make HTTP requests to the PokeAPI.
* Display the Pokemon data in a user-friendly format.
* Handle potential errors gracefully.
* Add some basic css styling.

**Example API Request (PokeAPI):**

```python
import requests

pokemon_name_or_id = "pikachu"
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}"

response = requests.get(url)
data = response.json()

# Extract relevant data from the JSON response
pokemon_name = data["name"]
pokemon_image = data["sprites"]["front_default"]
pokemon_types = [t["type"]["name"] for t in data["types"]]
pokemon_abilities = [a["ability"]["name"] for a in data["abilities"]]
pokemon_stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
```

**Evaluation Criteria:**

* **Functionality:** Does the application meet all the milestones?
* **Code quality:** Is the code well-structured, readable, and maintainable?
* **API integration:** Is the API integration implemented correctly and efficiently?
* **Error handling:** Are potential errors handled gracefully?
* **User interface:** Is the interface easy to use and understand?
