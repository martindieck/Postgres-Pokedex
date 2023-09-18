import psycopg2

def close(conn, cur):
    cur.close()
    conn.close()