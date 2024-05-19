#  HBase From Scratch in Python
#  Proyecto 3 Base de Datos 2
#  Universidad del Valle de Guatemala

# Creado por Javier Alvarado, Mario Guerra y Renatto Guzmán

# TODO: DONE Definir las estructuras de datos para almacenar las tablas y sus datos

# TODO: Implementar las funciones DDL (Data Definition Language)
#   TODO: Crear función create_table        - 5 puntos
#   TODO: Crear función list_tables         - 5 puntos
#   TODO: Crear función disable_table       - 3 puntos
#   TODO: Crear función is_table_enabled    - 3 puntos
#   TODO: Crear función alter_table         - 3 puntos
#   TODO: Crear función drop_table          - 3 puntos
#   TODO: Crear función drop_all_tables     - 3 puntos
#   TODO: Crear función describe_table      - 3 puntos

# TODO: Implementar las funciones DML (Data Manipulation Language)
#   TODO: Crear función put (insertar/actualizar datos)                     - 10 puntos
#   TODO: Crear función get (obtener datos)                                 - 8 puntos 
# 
#   TODO: Crear función scan (escanear datos)                               - 10 puntos 
#   DONE

#   TODO: Crear función delete (eliminar datos)                             - 5 puntos
#   TODO: Crear función delete_all (eliminar todos los datos)               - 5 puntos
#   TODO: Crear función count (contar registros)                            - 5 puntos
#   TODO: Crear función truncate (desactivar, eliminar y recrear tabla)     - 7 puntos

#   TODO: Crear función Insert many (insertar varios datos)                 - 5 puntos
#   TODO: Crear función Update many (actualizar  varios datos)              - 5 puntos

# TODO: Cargar set de datos inicial                     
# TODO: Crear funciones auxiliares si es necesario

# TODO: Interfaz gráfica

import json
import pandas as pd

from hbase import * 

# Crear tabla 
# column_families = ["Details", "Cast", "Metadata"]
# create("new2", column_families)

# Listar tablas
# list()

# Desactivar tablas
# disable('new')



## COUNT
# count("shows")

## SCAN
# scan("movies")

## DROP TABLE
# drop_table("movies")
# DROP ALL
# drop_all_tables()


table = "movies"
row_key = "0001"
family = "Cast"
qualifier = "Actor"
value = "Renatto Guzman"



#put(table, row_key, family, qualifier, value)

#scan("movies")
#scan("shows")

#get(table, row_key, family, qualifier)


# Inserta/actualiza datos en la tabla
#put(table, "0001", "Cast", "Extras", "Renatto Guzman")
#put(table, None, "Details", "Title", "New Show")

# Eliminar el actor "Morgan Freeman" de la fila "0001" en la tabla "movies"
#delete("movies", "0001", "Cast", "Actor", "Timestamp2")

# Eliminar la calificación (rating) de la fila "0002" en la tabla "shows"
#delete("shows", "0002", "Metadata", "Rating")

# Eliminar todos los datos de la fila "0001" en la tabla "movies"
#delete_all("movies", "0001")

# Eliminar todos los datos de la fila "0002" en la tabla "shows"
#delete_all("shows", "0002")

#truncate("movies")

#scan("movies")
