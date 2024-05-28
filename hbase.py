import time
from utils import *
from colorama import Fore, Style, init
import os
import json

# Métodos DDL
def create(table_name, column_families):
    if table_exists(table_name):
        print(f"Table '{table_name}' already exists")
        return
    
    initial_rows = [
        {
            "rowkey": "0001",
            **{family: {} for family in column_families}
        }
    ]
    
    save_file_data(table_name, initial_rows)
    print(f"Table '{table_name}' created successfully")
    
    status_file_path = "data/disable_table_status.json"
    
    # Verificar si el archivo de estado existe y cargar su contenido, o crear uno nuevo
    if os.path.exists(status_file_path):
        with open(status_file_path, "r") as status_file:
            table_status = json.load(status_file)
    else:
        table_status = {}
    
    # Añadir la nueva tabla con el estado `False`
    table_status[table_name] = False
    
    # Guardar el archivo de estado actualizado
    with open(status_file_path, "w") as status_file:
        json.dump(table_status, status_file, indent=2)
    
    print(f"Table '{table_name}' status added to '{status_file_path}'")


def list_table():
    start_time = time.time()
    
    directory = "data/"
    if not os.path.exists(directory):
        print("No tables found.")
        return

    tables = [f.replace('.json', '') for f in os.listdir(directory) if f.endswith('.json')]
    
    print(Fore.RED + "TABLE" + Style.RESET_ALL)
    if not tables:
        print("No tables found.")
    else:
        for table in tables:
            print(f'- {table}')
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{len(tables)} row(s) in {elapsed_time:.10f} seconds")

def disable(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return
    
    status_file_path = "data/disable_table_status.json"
    
    if not os.path.exists(status_file_path):
        print(f"No status file found. Table '{table_name}' might already be disabled.")
        return
    
    with open(status_file_path, "r") as status_file:
        table_status = json.load(status_file)
    
    if table_status.get(table_name) is True:
        print(f"Table '{table_name}' is already disabled")
        return
    
    table_status[table_name] = True
    
    with open(status_file_path, "w") as status_file:
        json.dump(table_status, status_file, indent=2)
    
    print(f"Table '{table_name}' has been disabled")


def enabled(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return
    
    status_file_path = "data/disable_table_status.json"
    
    if not os.path.exists(status_file_path):
        print(f"No status file found. Table '{table_name}' might already be enabled.")
        return
    
    with open(status_file_path, "r") as status_file:
        table_status = json.load(status_file)
    
    if table_status.get(table_name) is False:
        print(f"Table '{table_name}' is already enabled")
        return
    
    table_status[table_name] = False
    
    with open(status_file_path, "w") as status_file:
        json.dump(table_status, status_file, indent=2)
    
    print(f"Table '{table_name}' has been enabled")

def is_enabled(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return False
    
    status_file_path = "data/disable_table_status.json"
    
    if not os.path.exists(status_file_path):
        # If the status file does not exist, assume all tables are enabled
        return True
    
    with open(status_file_path, "r") as status_file:
        table_status = json.load(status_file)
    
    # Return the negation of the disabled status, default to True if not found
    enabled = not table_status.get(table_name, False)
    print(f"Table '{table_name}' enabled status: {enabled}")
    return enabled

def alter_table(table_name, new_column_families):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return

    table_data = get_file_data(table_name)
    
    # Check if the new column families already exist and add them if not
    for row in table_data:
        for family in new_column_families:
            if family not in row:
                row[family] = {}
    
    save_file_data(table_name, table_data)
    print(f"Table '{table_name}' altered successfully with new column families: {new_column_families}")

def drop_table(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return
    
    status_file_path = "data/disable_table_status.json"
    
    if not os.path.exists(status_file_path):
        print(f"No status file found. Cannot drop table '{table_name}'.")
        return
    
    with open(status_file_path, "r") as status_file:
        table_status = json.load(status_file)
    
    if table_status.get(table_name) != True:
        print(f"Table '{table_name}' must be disabled before it can be dropped.")
        return
    
    delete_table_file(table_name)
    
    # Remove the table status from the status file
    table_status.pop(table_name, None)
    with open(status_file_path, "w") as status_file:
        json.dump(table_status, status_file, indent=2)
    
    print(f"Table '{table_name}' has been dropped")

def drop_all_tables():
    tables = get_all_tables()
    if not tables:
        print("No tables found.")
        return
    
    status_file_path = "data/disable_table_status.json"
    
    if not os.path.exists(status_file_path):
        print("No status file found. Cannot drop tables.")
        return
    
    with open(status_file_path, "r") as status_file:
        table_status = json.load(status_file)
    
    for table in tables:
        if table_status.get(table) != True:
            print(f"Table '{table}' must be disabled before it can be dropped. Skipping.")
            continue
        
        delete_table_file(table)
        table_status.pop(table, None)
        print(f"Table '{table}' has been dropped")
    
    # Update the status file after dropping the tables
    with open(status_file_path, "w") as status_file:
        json.dump(table_status, status_file, indent=2)

    print("All eligible tables have been dropped.")

def describe_table(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return

    table_data = get_file_data(table_name)

    # Obtener las familias de columnas y los calificadores de columnas presentes en la tabla
    column_families = set()
    column_qualifiers = set()
    for row in table_data:
        for family, data in row.items():
            if family != 'rowkey':
                column_families.add(family)
                for qualifier in data.keys():
                    column_qualifiers.add(qualifier)

    print(f"\nTable '{table_name}' description:\n")
    
    # Necesito is table_enabled
    #print(f"Is enabled: {'Yes' if is_table_enabled(table_name) else 'No'}")
    print("Column Families:")
    for family in column_families:
        print(f"- {family}")
        for qualifier in column_qualifiers:
            print(f"  - {qualifier}")


# Métodos DML
def put(table_name, row_key, column_family, column_qualifier, value, timestamp=None):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return

    if timestamp is None:
        timestamp = int(time.time() * 1000)  # Generar un timestamp en milisegundos

    table_data = get_file_data(table_name)

    if row_key is None:  # Si no se proporciona un row_key, se genera uno nuevo
        row_key = f"{len(table_data) + 1:04d}"

    row_exists = False
    for row in table_data:
        if row['rowkey'] == row_key:
            row_exists = True
            if column_family not in row:
                row[column_family] = {}
            if column_qualifier not in row[column_family]:
                row[column_family][column_qualifier] = {}
            row[column_family][column_qualifier][f"Timestamp{timestamp}"] = value
            break

    if not row_exists:
        new_row = {
            'rowkey': row_key,
            column_family: {
                column_qualifier: {
                    f"Timestamp{timestamp}": value
                }
            }
        }
        table_data.append(new_row)

    save_file_data(table_name, table_data)
    print(f"Value '{value}' inserted/updated in table '{table_name}' at row '{row_key}', column '{column_family}:{column_qualifier}', timestamp '{timestamp}'")


def get(table_name, row_key, column_family=None, column_qualifier=None, timestamp=None):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return

    table_data = get_file_data(table_name)

    row_found = False
    for row in table_data:
        if row['rowkey'] == row_key:
            row_found = True
            if column_family is None:
                # Print the entire row
                print(f"\nRow '{row_key}' in table '{table_name}':")
                for family, data in row.items():
                    if family != 'rowkey':
                        for qualifier, values in data.items():
                            if isinstance(values, dict):
                                print(f"  Column:{family}:{qualifier}, {values}")
                            else:
                                for ts, value in values.items():
                                    print(f"  Column:{family}:{qualifier}:{ts}, {value}")
            elif column_family in row:
                if column_qualifier is None:
                    # Print the entire column family
                    print(f"\nColumn family '{column_family}' in row '{row_key}', table '{table_name}':")
                    for qualifier, values in row[column_family].items():
                        if isinstance(values, dict):
                            print(f"  Column:{column_family}:{qualifier}, {values}")
                        else:
                            for ts, value in values.items():
                                print(f"  Column:{column_family}:{qualifier}:{ts}, {value}")
                elif column_qualifier in row[column_family]:
                    if timestamp is None:
                        # Print all values for the column qualifier
                        print(f"\nColumn qualifier '{column_qualifier}' in row '{row_key}', column family '{column_family}', table '{table_name}':")
                        for ts, value in row[column_family][column_qualifier].items():
                            print(f"  {ts}, {value}")
                    else:
                        timestamp_str = f"Timestamp{timestamp}"
                        if timestamp_str in row[column_family][column_qualifier]:
                            # Print the value for the specified timestamp
                            value = row[column_family][column_qualifier][timestamp_str]
                            print(f"\nValue for row '{row_key}', column '{column_family}:{column_qualifier}', timestamp '{timestamp}' in table '{table_name}':")
                            print(f"  {value}")
                        else:
                            print(f"Timestamp '{timestamp}' not found for row '{row_key}', column '{column_family}:{column_qualifier}' in table '{table_name}'")
                else:
                    print(f"Column qualifier '{column_qualifier}' not found in row '{row_key}', column family '{column_family}' in table '{table_name}'")
            else:
                print(f"Column family '{column_family}' not found in row '{row_key}' in table '{table_name}'")

    if not row_found:
        print(f"Row '{row_key}' not found in table '{table_name}'")

def scan(table_name):
    
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return
    print("\n  TABLE: " + table_name.upper() + "\n")
        
        
    # TODO: Revisar que esté enabled la tabla
        
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
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    table_data = get_file_data(table_name)

    row = next((r for r in table_data if r["rowkey"] == row_key), None)
    if not row:
        print(f"Row '{row_key}' not found in table '{table_name}'")
        return
    if not column_family:
        table_data["data"].remove(row)
    elif column_family in row:
        if not column_qualifier:
            del row[column_family]
        elif column_qualifier in row[column_family]:
            if not timestamp:
                del row[column_family][column_qualifier]
            elif timestamp in row[column_family][column_qualifier]:
                del row[column_family][column_qualifier][timestamp]

    save_file_data(table_name, table_data)
    print(f"Deleted data from table '{table_name}', row '{row_key}'")

def delete_all(table_name, row_key):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return

    table_data = get_file_data(table_name)

    row = next((r for r in table_data if r["rowkey"] == row_key), None)
    if not row:
        print(f"Row '{row_key}' not found in table '{table_name}'")
        return

    table_data.remove(row)
    save_file_data(table_name, table_data)
    print(f"Deleted all data from table '{table_name}', row '{row_key}'")

def count(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return
        
    table_data = get_file_data(table_name)
    length = len(table_data)
    print("\n  COUNT OF TABLE '" + table_name.upper() + f"': {length}\n")

def truncate(table_name):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return

    table_data = get_file_data(table_name)
    
    # Preservar la estructura de la tabla (familias de columnas)
    column_families = {family: {} for family in table_data[0] if family != "rowkey"}

    # Crear un nuevo contenido vacío pero con la estructura de la tabla original
    truncated_table_data = []

    for row in table_data:
        truncated_row = {"rowkey": row["rowkey"]}
        truncated_row.update(column_families)
        truncated_table_data.append(truncated_row)

    save_file_data(table_name, truncated_table_data)
    print(f"Table '{table_name}' has been truncated")

def update_many(table_name, updates):
    if not table_exists(table_name):
        print(f"Table '{table_name}' does not exist")
        return

    table_data = get_file_data(table_name)
    for update in updates:
        row_key = update['rowkey']
        for column_family, column_data in update.items():
            if column_family != 'rowkey':
                for column_qualifier, value in column_data.items():
                    timestamp = int(time.time() * 1000)  # Generar un timestamp en milisegundos
                    put(table_name, row_key, column_family, column_qualifier, value, timestamp)

    print(f"Updated {len(updates)} rows in table '{table_name}'")