from utils.fetch_data import fetch_data

def extract_data(category_data, columns, url):
    if category_data is not None:
        count = category_data["count"]
        row_list = []
        row = []

        for i in range(count):
            fetch_url = f'{url}{i+1}/'
            row_data = fetch_data(fetch_url)

            if row_data is not None:
                for column in columns:
                    if type(column) == list:
                        row.append(row_data[column[0]]['url'].rsplit("/", 2)[-2])
                    else:
                        row.append(row_data[column])
            row_list.append(tuple(row))
            row = []
        return (row_list)
    else:
        print("Could not fetch data.")
        return None