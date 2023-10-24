import math
from tqdm import tqdm
from utils.fetch_data import fetch_data
from utils.navigate_data import navigate_data

def extract_data(category_data, keys, url):
    '''
    extract_data(category_data, keychain, url)\n
    category_data = dictionary that contains the general resource information ()\n
    keys = This is a list of key chains, where each key chain is itself a list of keys or indices to navigate through the nested data structure.\n
    keys example: [['id'],['generation','url']]\n
    url = general url for target resource example: (https://pokeapi.co/api/v2/move/)
    '''
    
    if category_data is not None: # Check that the passed data exists properly.
        count_total = category_data["count"] # Obtain the total count of entries for the specified resource.
        offset = '?offset=-21' # Uses the "offset=-21" term to cycle to the last entry
        last_page_url = f'{url}{offset}/' # Obtain the url for the dictionary containing last page results for that resource

        # Invalid ids are those that start counting from 10,000 onward (ex. 10001, 10054, etc.). They represent incomplete/missing resource entries in the API.
        # To know the exact count of valid ids, the exact id of the last invalid entry is retrieved (ex. 10053) and a subtraction is made between that and the total count.
        # For example, if the total count is 362 and the last invalid entry is 10052, the true count of valid entries would be 309.
        
        last_page_data = fetch_data(last_page_url)
        navigated_last_page_data = navigate_data(last_page_data,[['results', -1, 'url']])
        if navigated_last_page_data[0] >= 10000:
            true_count = count_total - (navigated_last_page_data[0] - 10000) - 1
        else:
            true_count = count_total

        print('Commencing data extraction. Valid records found: ' + str(true_count)) # QoL statement that announces the total valid records found.

        row_list = [] # Initializing empty list for final results.

        # Loop that initializes once per valid entry. Using the 'tqdm' package to create a load bar for QoL.
        for i in tqdm (range (true_count), desc="Extracting"):
            
            # Creates unique url that gets passed into the 'fetch_data' function for calling the API.
            fetch_url = f'{url}{i+1}/'
            row_data = fetch_data(fetch_url)

            # Using the 'navigate_data' function and the list of 'keys' to extract the desired data from the results.
            if row_data is not None:
                row = navigate_data(row_data, keys)
                row_list.append(tuple(row)) # Creates a tuple containing all individual row information and appends it to final result list.
        return (row_list)
    else:
        print("Could not fetch data.")
        return None