
from utils import *


# Métodos DDL
def create_table(self, table_name, column_families):
    pass

def list_tables(self):
    pass

def disable_table(self, table_name):
    pass

def is_table_enabled(self, table_name):
    pass

def alter_table(self, table_name, new_column_families):
    pass

def drop_table(self, table_name):
    pass

def drop_all_tables(self):
    pass

def describe_table(self, table_name):
    pass

# Métodos DML
def put(self, table_name, row_key, column_family, column_qualifier, value, timestamp=None):
    pass

def get(self, table_name, row_key, column_family=None, column_qualifier=None, timestamp=None):
    pass

def scan(table_name):
    
    if not table_exists(table_name):
        print("Table does not exist")
        return
    print("\n  TABLA = " + table_name.upper() + "\n")
        
    table_data = get_file_data(table_name)
    print("ROWKEY   COLUMN+CELL")
    for row in table_data:
        rowkey = row['rowkey']
        for column_family, column_data in row.items():
            if column_family != 'rowkey':
                for column_qualifier, values in column_data.items():
                    if isinstance(values, dict):
                        print(f" {rowkey}    Column:{column_family}:{column_qualifier}, {values}")
                    else:
                        for timestamp, value in values.items():
                            print(f" {rowkey}    Column:{column_family}:{column_qualifier}:{timestamp}, {value}")
            
    
    

def delete(self, table_name, row_key, column_family=None, column_qualifier=None, timestamp=None):
    pass

def delete_all(self, table_name, row_key):
    pass

def count(self, table_name):
    pass

def truncate(self, table_name):
    pass