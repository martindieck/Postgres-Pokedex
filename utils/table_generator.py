from utils.create_table import create_table
from utils.fetch_data import fetch_data
from utils.extract_data import extract_data
from utils.insert_data import insert_data

class Table:
    '''
    Class parameters:\n
    conn = psycopg connection\n
    cur = psycopg cursor\n
    url = category url\n
    table_name = desired table name\n
    fields = desired table fields in format: id int PRIMARY KEY, name text\n
    keys = list of desired fields to extract from API (if url inside dictionary, use list as so: ['main_region','url'])\n
    '''
    def __init__(self, conn, cur, url, table_name, fields, keys):
        self.conn = conn
        self.cur = cur
        self.url = url
        self.name = table_name
        self.fields = fields
        self.keys = keys
        print('Creating table object.')

        
    def create_table(self):
        create_table(self.name, self.fields, self.cur)

    def fetch_data(self):
        return fetch_data(self.url)
    
    def extract_data(self, category_data):
        return extract_data(category_data, self.keys, self.url)
    
    def insert_data(self, extracted_data):
        insert_data(self.cur, self.name, extracted_data)