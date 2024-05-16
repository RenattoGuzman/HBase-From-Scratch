class HBase:
    def __init__(self):
        self.tables = {}  # Diccionario para almacenar las tablas {nombre_tabla: datos_tabla}

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

    def scan(self, table_name, start_row=None, stop_row=None, column_family=None, column_qualifier=None):
        pass

    def delete(self, table_name, row_key, column_family=None, column_qualifier=None, timestamp=None):
        pass

    def delete_all(self, table_name, row_key):
        pass

    def count(self, table_name):
        pass

    def truncate(self, table_name):
        pass