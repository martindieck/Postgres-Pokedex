import psycopg2
import csv
from io import StringIO

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

    print('Attempting data insertion.') # QoL message for status.

    # Creating CSV buffer for data insertion
    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerows(extracted_data)
    csv_buffer.seek(0)

    try:
        cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV", csv_buffer)
        print('Data insertion using COPY successful.')
    except Exception as e:
        print(f"Error inserting data using COPY: {e}")