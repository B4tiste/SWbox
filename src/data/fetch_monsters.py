import requests
import json
import os

def fetch_all_data(start_url):
    """Récupère toutes les données en suivant les liens 'next'."""
    all_results = []
    next_url = start_url
    page_number = 1

    while next_url:
        print(f"Fetching data from page {page_number}...")
        response = requests.get(next_url)

        if response.status_code != 200:
            print(f"Failed to fetch data from {next_url}. Exiting...")
            return {"monsters": all_results}

        data = response.json()
        fetched_monsters_count = len(data["results"])
        print(f"Fetched {fetched_monsters_count} monsters from page {page_number}.")

        all_results.extend(data["results"])
        next_url = data["next"]
        page_number += 1

    return {"monsters": all_results}

def load_existing_data(file_path):
    """Charge les données existantes depuis le fichier JSON."""
    if os.path.exists(file_path):
        with open(file_path, "r") as infile:
            return json.load(infile)
    return {"monsters": []}

def find_new_monsters(existing_monsters, fetched_monsters):
    """Trouve les nouveaux monstres en comparant les anciens et les nouveaux."""
    existing_ids = {monster["id"] for monster in existing_monsters}
    new_monsters = [monster for monster in fetched_monsters if monster["id"] not in existing_ids]
    return new_monsters

if __name__ == "__main__":
    start_url = "https://swarfarm.com/api/v2/monsters/"
    file_path = "monsters.json"

    print("Starting data fetch from SWARFARM...")
    all_data = fetch_all_data(start_url)

    print("Loading existing data...")
    existing_data = load_existing_data(file_path)

    print("Finding new monsters...")
    new_monsters = find_new_monsters(existing_data["monsters"], all_data["monsters"])

    # Affiche les nouveaux monstres
    if new_monsters:
        print(f"\nNew monsters found: {len(new_monsters)}")
        for monster in new_monsters:
            print(f"- {monster['name']} (ID: {monster['id']})")
    else:
        print("\nNo new monsters found.")

    # Sauvegarder les données mises à jour dans un fichier JSON
    with open(file_path, "w") as outfile:
        json.dump(all_data, outfile, indent=4)

    print(f"\nData fetching completed. Total monsters saved: {len(all_data['monsters'])}. Data saved to {file_path}.")
