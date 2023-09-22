from utils.connect import connect
from utils.data_pipeline import data_pipeline

conn, cur = connect()
url = 'https://pokeapi.co/api/v2/type/'
table_name = 'pokemon_types'
table_fields = 'id SERIAL PRIMARY KEY, name TEXT, intro_generation INTEGER'
api_fields = [['id'],['name'],['generation','url']]

data_pipeline(conn, cur, url, table_name, table_fields, api_fields)