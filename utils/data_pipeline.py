import psycopg2
from utils.close import close
from utils.table_generator import Table

def data_pipeline(conn, cur, url, table_name, table_fields, api_fields):

    table_object = Table(conn, cur, url, table_name, table_fields, api_fields)

    table_object.create_table()

    data = table_object.fetch_data()

    extracted_data = table_object.extract_data(data)

    table_object.insert_data(extracted_data)

    conn.commit()

    close(conn, cur)