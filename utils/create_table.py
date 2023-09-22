import psycopg2

def create_table(table_name, fields, cur, if_not_exists=True):
    '''
    create_table(table_name, fields, cur, if_not_exists=True) \n
    table_name = table name as a string.\n
    fields = field names separated by commas and specifying data types: id SERIAL PRIMARY KEY, name TEXT\n
    cur = cursor object created from previous connection.\n
    if_not_exists (default True) = change to False for a "CREATE TABLE" statement without the "IF NOT EXISTS"\n
    '''

    print('Creating table with name: ' + table_name) # Added status message for QoL purposes.
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
    
    cur.execute(query) # Using string formatting to avoid SQL Injection exposure.