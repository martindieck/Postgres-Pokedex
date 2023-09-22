import psycopg2

def insert_data(cur, table_name, extracted_data):
    '''
    insert_data(cur, table_name, extracted_data)\n
    cur = created cursor through psycopg.\n
    table_name = previously created table name to insert data into.\n
    extracted_data = list of tuples containing extracted and selected data from the API ready for insertion.\n
    '''
    
    if not extracted_data:  # Handle the case where extracted_data list is empty.
        print("No data to insert.")
        return

    # Dynamically calculating the number of required parameters.
    num_params = len(extracted_data[0])     # Obtaining the length of an individual tuple inside the results.
    placeholders = ', '.join(['%s'] * num_params)   # Creating the necessary amount of placeholders for query.
    query = f"INSERT INTO {table_name} VALUES ({placeholders})" # Preparing the final query.
    
    print('Attempting data insertion.') # QoL message for status.
    try:
        cur.executemany(query, extracted_data)  # Using string formatting to avoid SQL Injection exposure.
        print('Data insertion successful.')
    except Exception as e:
        print(f"Error inserting data: {e}")