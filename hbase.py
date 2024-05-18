
from utils import *


# Métodos DDL
def create_table(table_name, column_families):
    pass

def list_tables():
    pass

def disable_table(table_name):
    pass

def is_table_enabled(table_name):
    pass

def alter_table(table_name, new_column_families):
    pass

def drop_table(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return
    
    delete_table_file(table_name)
    print(f"Table '{table_name}' has been dropped")

def drop_all_tables():
    tables = get_all_tables()
    if not tables:
        print("No tables found.")
        return
    for table in tables:
        delete_table_file(table)
    print("All tables have been dropped.")

def describe_table(table_name):
    pass

# Métodos DML
def put(table_name, row_key, column_family, column_qualifier, value, timestamp=None):
    pass

def get(table_name, row_key, column_family=None, column_qualifier=None, timestamp=None):
    pass

def scan(table_name):
    
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return
    print("\n  TABLE: " + table_name.upper() + "\n")
        
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

def delete(table_name, row_key, column_family=None, column_qualifier=None, timestamp=None):
    pass

def delete_all(table_name, row_key):
    pass

def count(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return
        
    table_data = get_file_data(table_name)
    length = len(table_data)
    print("\n  COUNT OF TABLE " + table_name.upper() + f": {length}\n")

def truncate(table_name):
    pass