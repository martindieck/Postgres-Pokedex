import psycopg2

def connect():
    conn = psycopg2.connect("dbname=postgres user=postgres password=pokedex123") # Change dbname, user and password according to user's specs.
    cur = conn.cursor()
    print('Connection to database successful.') # Added status message for QoL.
    return conn, cur