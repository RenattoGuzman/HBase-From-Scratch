import json
import os


def table_exists(table_name):
    file_path = "data/" + table_name + ".json"
    return os.path.exists(file_path)

def get_file_data(table_name):
    file_path = "data/" + table_name + ".json"
    file = open(file_path)
    data = json.load(file)
    return data

def delete_table_file(table_name):
    file_path = "data/" + table_name + ".json"
    os.remove(file_path)

def get_all_tables():
    return [f.split(".")[0] for f in os.listdir("data") if f.endswith(".json")]

def save_file_data(table_name, table_data):
    file_path = f"data/{table_name}.json"

    try:
        with open(file_path, "w") as file:
            json.dump(table_data, file, indent=2)
        print(f"Table '{table_name}' data saved successfully.")
    except Exception as e:
        print(f"Error saving table '{table_name}' data: {e}")
