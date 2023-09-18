from utils.connect import connect
from utils.close import close
from utils.create_table import create_table
from utils.fetch_data import fetch_data

base_url = 'https://pokeapi.co/api/v2/generation/'  # Replace with the actual API URL
generation_data = fetch_data(base_url)

if generation_data is not None:
    count = generation_data["count"]
    gen_list = []

    for i in range(count):
        generation_url = f'{base_url}{i+1}/'
        data = fetch_data(generation_url)

        if data is not None:
            temp = (
                data["id"],
                data["name"],
                data["main_region"]["url"].rsplit("/", 2)[-2]
            )
            gen_list.append(temp)

    print(gen_list)
else:
    print("Could not fetch data.")