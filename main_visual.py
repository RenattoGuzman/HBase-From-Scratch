#  HBase From Scratch in Python
#  Proyecto 3 Base de Datos 2
#  Universidad del Valle de Guatemala

# Creado por Javier Alvarado, Mario Guerra y Renatto Guzmán

import json
import pandas as pd
import io
import sys
from hbase import * 
import tkinter as tk

# Color palette
colors = {
    "background": "#003249",
    "primary": "#007ea7",
    "secondary": "#9ad1d4",
    "accent1": "#80ced7",
    "accent2": "#6695C2"
}

fun_dict = {
    "create": create,
    "list_table": list_table,
    "disable": disable,
    "enable": enabled,
    "is_enabled": is_enabled,
    "describe": describe_table,
    "drop": drop_table,
    "dropall": drop_all_tables,
    "get": get,
    "put": put,
    "alter": alter_table,
    "delete": delete,
    "deleteall": delete_all,
    "scan": scan,
    "count": count,
    "truncate": truncate,
    "update_many": update_many,
    "search": search_by_index,
    # Para agregar una funcion solamente se agrega el nombre de la funcion y el nombre del comando
}
list_of_commands = list(fun_dict.keys())


# Create the main window
root = tk.Tk()
root.title("HBase from Scratch")
root.configure(bg=colors["background"])

# Function to handle command execution
def execute_command():
    input_text = command_entry.get()
    command_list = input_text.split(" ")
    command, *args = command_list
    output_text.delete("1.0", tk.END)

    if command in list_of_commands:
        # Capture the printed output
        
        captured_output = io.StringIO()
        sys.stdout = captured_output  # Redirect stdout to the StringIO object

        try:
            if command == "alter":
                if len(args) < 2:
                    raise TypeError("Invalid arguments")
                table_name = args[0]
                new_column_families = args[1:]
                fun_dict[command](table_name, new_column_families)
            elif command == "search":
                if len(args) != 4:
                    raise TypeError("Invalid arguments")
                table_name, column_family, column_qualifier, value = args
                result_row_keys = fun_dict[command](table_name, column_family, column_qualifier, value)
                print(f"Rows with {column_family}:{column_qualifier}='{value}': {result_row_keys}")
            elif command == "create":
                if len(args) < 2:
                    raise TypeError("Invalid arguments")
                table_name = args[0]
                column_families = args[1].split(',')
                fun_dict[command](table_name, column_families)
            elif command == "put":
                if len(args) < 5:
                    raise TypeError("Invalid arguments")
                table_name, row_key, column_family, column_qualifier, value = args
                fun_dict[command](table_name, row_key, column_family, column_qualifier, value)
            elif command == "get":
                if len(args) != 5:
                    raise TypeError("Invalid arguments")
                table_name, row_key, column_family, column_qualifier, timestamp = args
                if timestamp == "":
                    timestamp = None
                fun_dict[command](table_name, row_key, column_family, column_qualifier, timestamp)
            else:
                fun_dict[command](*args)
        except TypeError:
            output_text.insert(tk.END, f"Invalid arguments, type '{command}?' for more information\n")

        sys.stdout = sys.__stdout__  # Reset stdout to its original value

        # Get the captured output and insert it into the output_text widget
        captured_output_str = captured_output.getvalue()
        output_text.insert(tk.END, captured_output_str)

    elif command == "exit":
        root.quit()
    else:
        output_text.insert(tk.END, "Command not found, type 'help' for a list of commands\n")
    #command_entry.delete(0, tk.END)

title_frame = tk.Frame(root, bg=colors["background"])
title_frame.pack(pady=20)

title_label = tk.Label(title_frame, text="HBase from Scratch", font=("Tahoma", 32, "bold"), bg=colors["background"], fg=colors["secondary"])
title_label.pack()


command_frame = tk.Frame(root, bg=colors["background"])
command_frame.pack(pady=20)

command_label = tk.Label(command_frame, text="Entrada de texto", font=("Tahoma", 12, "bold"), bg=colors["background"], fg=colors["secondary"])
command_label.pack(side=tk.LEFT, padx=5)

command_entry = tk.Entry(command_frame, font=("Lucida Console", 14), bg=colors["accent1"], fg=colors["background"])
command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

execute_button = tk.Button(command_frame, text="Execute", font=("Tahoma", 12, "bold"), bg=colors["primary"], fg="white", command=execute_command)
execute_button.pack(side=tk.RIGHT, padx=5)

# Create the output area
output_frame = tk.Frame(root, bg=colors["background"])
output_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

output_text = tk.Text(output_frame, font=("Lucida Console", 12), bg=colors["accent1"], fg=colors["background"])
output_text.pack(fill=tk.BOTH, expand=True)


# Start the main event loop
root.mainloop()