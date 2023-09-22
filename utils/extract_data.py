from utils.fetch_data import fetch_data
from utils.navigate_data import navigate_data

def extract_data(category_data, columns, url):
    if category_data is not None:
        count = category_data["count"]
        row_list = []

        if url.rsplit("/", 2)[-2] == 'pokemon':
            count = 1017

        for i in range(count):
            fetch_url = f'{url}{i+1}/'
            row_data = fetch_data(fetch_url)

            if row_data is not None:
                row = navigate_data(row_data, columns)
                row_list.append(tuple(row))
        return (row_list)
    else:
        print("Could not fetch data.")
        return None