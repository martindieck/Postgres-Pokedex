import psycopg2

def create_table(table_name, fields, cur, if_not_exists = True):
    if if_not_exists:
        cur.execute("""
                CREATE TABLE IF NOT EXISTS """ + table_name +  """ ( """
                    + fields +
                """);
                """)
    else:
        cur.execute("""
                CREATE TABLE """ + table_name +  """ ( """
                    + fields +
                """);
                """)