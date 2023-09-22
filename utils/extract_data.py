import math
from utils.fetch_data import fetch_data
from utils.navigate_data import navigate_data

def extract_data(category_data, columns, url):
    if category_data is not None:
        count_total = category_data["count"]
        offset = '?offset=-21'
        fetch_true_count = f'{url}{offset}/'
        true_count = count_total - (navigate_data(fetch_data(fetch_true_count),[['results', 19, 'url']])[0] - 10000) - 1

        print('Commencing data extraction. Valid records found: ' + str(true_count))

        row_list = []

        for i in range(true_count):
            if (i + 1) % (true_count // 5) == 0:
                progress = math.ceil(((i + 1) / true_count) * 100)
                print(f"Progress: {int(progress)}%" + f" - Record #{i + 1}")

            fetch_url = f'{url}{i+1}/'
            row_data = fetch_data(fetch_url)

            if row_data is not None:
                row = navigate_data(row_data, columns)
                row_list.append(tuple(row))
        return (row_list)
    else:
        print("Could not fetch data.")
        return None