from utils.connect import connect
from utils.data_pipeline import data_pipeline

conn, cur = connect()
url = 'https://pokeapi.co/api/v2/generation/'
table_name = 'generations'
table_fields = 'id SERIAL PRIMARY KEY, name VARCHAR(40), main_region INTEGER'
api_fields = ['id','name',['main_region','url']]

data_pipeline(conn, cur, url, table_name, table_fields, api_fields)