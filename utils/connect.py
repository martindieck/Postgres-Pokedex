import psycopg2

def connect():
    host = 'pokedex-db.co6jyeobbdsz.us-east-2.rds.amazonaws.com'
    port = 5432
    database = 'pokedex_db'
    user = 'postgres'
    password = 'pokedex123'

    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cur = conn.cursor()
    print('Connection to database successful.') # Added status message for QoL.
    return conn, cur