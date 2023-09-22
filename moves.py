from utils.connect import connect
from utils.data_pipeline import data_pipeline

conn, cur = connect()
url = 'https://pokeapi.co/api/v2/move/'
table_name = 'moves'
table_fields = '''id SERIAL PRIMARY KEY,
                name TEXT,
                move_type INTEGER,
                power INTEGER,
                pp INTEGER,
                accuracy INTEGER,
                priority INTEGER,
                effect_chance INTEGER,
                damage_class TEXT,
                min_hits INTEGER,
                max_hits INTEGER,
                min_turns INTEGER,
                max_turns INTEGER,
                drain INTEGER,
                healing INTEGER,
                ailment TEXT,
                crit_rate INTEGER,
                ailment_chance INTEGER,
                flinch_chance INTEGER,
                stat_chance INTEGER,
                generation INTEGER,
                effect TEXT,
                short_effect TEXT,
                flavor_text TEXT'''
api_fields = [['id'],['name'],['type','url'],['power'],['pp'],['accuracy'],['priority'],['effect_chance'],['damage_class','name'],['meta','min_hits'],['meta','max_hits'],['meta','min_turns'],['meta','max_turns'],['meta','drain'],['meta','healing'],['meta','ailment','name'],['meta','crit_rate'],['meta','ailment_chance'],['meta','flinch_chance'],['meta','stat_chance'],['generation','url'],['effect_entries',-1,'effect'],['effect_entries',-1,'short_effect'],['flavor_text_entries', -3, 'flavor_text']]

data_pipeline(conn, cur, url, table_name, table_fields, api_fields)