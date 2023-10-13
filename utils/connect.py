import psycopg2
import configparser

def connect():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Database connection parameters
    host = config.get('database', 'host')
    port = config.get('database', 'port')
    database = config.get('database', 'database')
    user = config.get('database', 'user')
    password = config.get('database', 'password')
    
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