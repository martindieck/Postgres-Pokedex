import psycopg2

def insert_data(cur, table_name, extracted_data):
    if not extracted_data:
        print("No data to insert.")
        return
    
    num_params = len(extracted_data[0])
    placeholders = ', '.join(['%s'] * num_params)
    query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    
    try:
        cur.executemany(query, extracted_data)
    except Exception as e:
        print(f"Error inserting data: {e}")