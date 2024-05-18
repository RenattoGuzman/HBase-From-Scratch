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