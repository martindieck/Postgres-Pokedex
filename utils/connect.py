import psycopg2

def connect():
    conn = psycopg2.connect("dbname=postgres user=postgres password=pokedex123")
    cur = conn.cursor()
    print('Connection to database successful.')
    return conn, cur