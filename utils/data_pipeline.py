import psycopg2
import time
from utils.close import close
from utils.table_generator import Table

def data_pipeline(conn, cur, url, table_name, table_fields, api_fields):
    start = time.time()

    table_object = Table(conn, cur, url, table_name, table_fields, api_fields)

    table_object.create_table()

    data = table_object.fetch_data()

    extracted_data = table_object.extract_data(data)

    table_object.insert_data(extracted_data)

    print('Committing changes.')
    conn.commit()

    close(conn, cur)
    
    end =  time.time()

    runtime = end - start

    runtime = end-start

    runtime_formatted = time.strftime('%H:%M:%S', time.gmtime(runtime))

    print('End of process. Runtime: ' + runtime_formatted)