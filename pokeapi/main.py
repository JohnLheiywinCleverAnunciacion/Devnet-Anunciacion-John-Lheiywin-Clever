import random

import requests

def fetch_pokemon_data(pokemon_name):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().strip()}"

    try:

        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            return {

                "name": data["name"],

                "height": data["height"],

                "weight": data["weight"]

            }

        elif response.status_code == 404:

            print(f"Error: Pokémon '{pokemon_name}' not found on API.")

            return None

        else:

            print(f"Error: Unexpected status code {response.status_code}.")

            return None

    except requests.exceptions.RequestException as e:

        print(f"Network Error: {e}")

        return None

def play_game():

    pokemon_pool = ["pikachu", "charizard", "cinderace", "fuecoco", "arcanine"]

    print("Welcome to the PokeAPI Pokémon Guessing Game!")

    print("Fetching data from the Pokémon database...")

    selected_pokemon_name = random.choice(pokemon_pool)

    pokemon_data = fetch_pokemon_data(selected_pokemon_name)

    if not pokemon_data:

        print("Could not load game data due to an error.")

        return

    attempts = 3

    correct_name = pokemon_data["name"]

    print("\n--- A Wild Pokémon Appears! ---")

    print(f"Height: {pokemon_data['height']} decimeters")

    print(f"Weight: {pokemon_data['weight']} hectograms")

    print("Can you guess who it is?")

    while attempts > 0:

        guess = input(f"\n[{attempts} attempts left] Your guess: ").strip().lower()

        if not guess:

            print("Please enter a valid name.")

            continue

        if guess == correct_name:

            print(f"\n Congratulations! You guessed it right! It is indeed {correct_name.capitalize()}!")

            return

        else:

            attempts -= 1

            if attempts > 0:

                print("Incorrect! Try again.")

    print(f"\n Game Over! You've run out of attempts. The correct Pokémon was: {correct_name.capitalize()}.")

if __name__ == "__main__":

    play_game()
 