from utils.connect import connect
from utils.data_pipeline import data_pipeline

conn, cur = connect()
url = 'https://pokeapi.co/api/v2/region/'
table_name = 'regions'
table_fields = '''id SERIAL PRIMARY KEY,
                name TEXT'''
api_fields = [['id'],['name']]

data_pipeline(conn, cur, url, table_name, table_fields, api_fields)