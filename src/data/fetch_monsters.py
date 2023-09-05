import requests
import json

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

if __name__ == "__main__":
    start_url = "https://swarfarm.com/api/v2/monsters/"
    print("Starting data fetch from SWARFARM...")
    all_data = fetch_all_data(start_url)

    # Sauvegarder les données dans un fichier JSON
    with open("monsters.json", "w") as outfile:
        json.dump(all_data, outfile, indent=4)

    print(f"\nData fetching completed. Total monsters saved: {len(all_data['monsters'])}. Data saved to monsters.json.")
