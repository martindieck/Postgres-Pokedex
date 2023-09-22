from utils.connect import connect
from utils.data_pipeline import data_pipeline

conn, cur = connect()
url = 'https://pokeapi.co/api/v2/pokemon/'
table_name = 'pokemon'
table_fields = '''id SERIAL PRIMARY KEY,
                name TEXT,
                type_one INTEGER,
                type_two INTEGER,
                hp INTEGER,
                attack INTEGER,
                defense INTEGER,
                sp_attack INTEGER,
                sp_defense INTEGER,
                speed INTEGER,
                height INTEGER,
                weight INTEGER,
                base_experience INTEGER,
                normal_image TEXT,
                shiny_image TEXT'''
api_fields = [['id'],['name'],['types',0,'type','url'],['types',1,'type','url'],['stats',0,'base_stat'],['stats',1,'base_stat'],['stats',2,'base_stat'],['stats',3,'base_stat'],['stats',4,'base_stat'],['stats',5,'base_stat'],['height'],['weight'],['base_experience'],['sprites','other','official-artwork','front_default'],['sprites','other','official-artwork','front_shiny']]

data_pipeline(conn, cur, url, table_name, table_fields, api_fields)