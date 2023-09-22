import psycopg2
import time
from utils.close import close
from utils.table_generator import Table

def data_pipeline(conn, cur, url, table_name, table_fields, keys):
    '''
    data_pipeline(conn, cur, url, table_name, table_fields, keys)\n
    conn = created connection with database through psycopg\n
    cur = created cursor through psycopg\n
    url = general url for target resource example: (https://pokeapi.co/api/v2/move/)\n
    table_name = desired table name as a string\n
    table_fields = field names separated by commas and specifying data types: id SERIAL PRIMARY KEY, name TEXT\n
    keys = This is a list of key chains, where each key chain is itself a list of keys or indices to navigate through the nested data structure.\n
    keys example: [['id'],['generation','url']]
    '''
    
    start = time.time() # Start the program countdown for runtime calculation.

    table_object = Table(conn, cur, url, table_name, table_fields, keys) # Create Table object to avoid passing down repeating parameters.

    table_object.create_table()

    data = table_object.fetch_data() # Fetch generalized resource data for count calculation.

    extracted_data = table_object.extract_data(data) # Get final resource list containing each row with its specified data.

    table_object.insert_data(extracted_data)

    print('Committing changes.') # Announcing the commit for QoL
    conn.commit()

    close(conn, cur) # Closing the connection to prevent adverse effects and slowdowns.
    
    end =  time.time() # Finish runtime measure.

    runtime = end - start

    runtime_formatted = time.strftime('%H:%M:%S', time.gmtime(runtime)) # Format the runtime to readable HH:MM:SS format.

    print('End of process. Runtime: ' + runtime_formatted) # Announce process end and print total runtime for measuring and KPI purposes.