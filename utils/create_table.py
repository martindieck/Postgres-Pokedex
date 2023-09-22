import psycopg2

def create_table(table_name, fields, cur, if_not_exists=True):
    print('Creating table with name: ' + table_name)
    if if_not_exists:
        query = """
                CREATE TABLE IF NOT EXISTS {} (
                    {}
                );
                """.format(table_name, fields)
    else:
        query = """
                CREATE TABLE {} (
                    {}
                );
                """.format(table_name, fields)
    
    cur.execute(query)