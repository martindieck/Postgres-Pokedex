from utils.connect import connect
from utils.data_pipeline import data_pipeline

conn, cur = connect()
url = 'https://pokeapi.co/api/v2/ability/'
table_name = 'abilities'
table_fields = '''id SERIAL PRIMARY KEY,
                name TEXT,
                is_main_series BOOLEAN,
                generation INTEGER,
                effect TEXT,
                short_effect TEXT,
                flavor_text TEXT'''
api_fields = [['id'],['name'],['is_main_series'],['generation','url'],['effect_entries',-1,'effect'],['effect_entries',-1,'short_effect'],['flavor_text_entries', -3, 'flavor_text']]

data_pipeline(conn, cur, url, table_name, table_fields, api_fields)