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

# Presentación de H-Base From Scratch

# Listar tablas
# list_table()

# Crear tabla sin column_families
"""""

column_families = []
create("prueba1", column_families)

"""""

# Crear tabla con una column_family

"""""
column_families = ["CF1"]
create("prueba1", column_families)
"""""

# Listar tablas
# list_table()

# Crear tabla con tres column_family
"""""
column_families = ["CF1", "CF2", "CF3"]
create("prueba2", column_families)
"""""

# Describe prueba2
# describe_table("prueba2")

#Listar tablas
#list_table()


# Insertar un registro a CF1,CF2,CF3

"""""
table = "prueba2"
row_key = "0001"
family = ["CF1","CF2","CF3"]
qualifier = "abc"
value = "CQ"

put(table, row_key, family, qualifier, value)

"""""

# Actualizar Celda CF2

"""""
table = "prueba2"
row_key = "0001"
family = "CF3"
qualifier = "abc"
value = "MarioGM54"


put(table, row_key, family, qualifier, value)

"""""

# Revisar is enable prueba2
#is_enabled("prueba2")


# Desactivar tabla 2
#disable('prueba2')


# Insertar solo un valor CQ (NO DEBE PERMITIR)

"""""
table = "prueba2"
row_key = "XASXS"
family = "dSXSA"
qualifier = "OCHOA"
value = "CQ"
"""""

#put(table, row_key, family, qualifier, value)

# Revisar is disabled

#is_enabled("prueba2")

# Deshabilitar "prueba2" 
#disable("prueba2")



# Habilitar "prueba2"
#enabled("prueba2")

# Habilitar "prueba2" (indicar que ya esta habilitada)
#enabled("prueba2")


# Insertar un registro en "prueba2" con un valor en un CQ unicamente
""""
table = "prueba2"
row_key = "00002"
family = "Nose"
qualifier = "Hola"
value = ""

put(table, row_key, family, qualifier, value)

"""""

#Insertar un registro en "prueba1" con un valor en un CQ unicamente

"""""
table = "prueba1"
row_key = "00002"
family = "Nose"
qualifier = "Hola"
value = ""


put(table, row_key, family, qualifier, value)

"""""

# Obtener primer registro de "prueba2" sin especificar CF ni CQ en formato legible

"""""
table = "prueba2"
row_key = "0001"
family = ""
qualifier = ""
timestamp = ""

get(table, row_key, family, qualifier, timestamp)
"""""

# Obtener primer registro de "prueba2" con CF especificado en formato legible

"""""
table = "prueba2"
row_key = "0001"
family = "CF1"
qualifier = ""
timestamp = ""

get(table, row_key, family, qualifier, timestamp)
"""""


# Obtener primer registro de "prueba2" con CF:CQ especificados en formato legible


table = "prueba2"
row_key = "0001"
family = "CF1"
qualifier = "abc"
timestamp = ""


get(table, row_key, family, qualifier, timestamp)


# Obtener primer registro de "prueba2" con CF:CQ y version especificados en formato legible


"""""
table = "prueba2"
row_key = "0001"
family = "CF3"
qualifier = "abc"
timestamp = "Timestamp1717041518593"

get(table, row_key, family, qualifier)
"""""



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

"""
updates = [
    {
        "rowkey": "0001",
        "Details": {
            "Title": {
                "Timestamp1720000000000": "The Shawshank Redemption - Updated"
            }
        },
        "Cast": {
            "Actor": {
                "Timestamp1720000000000": "Updated Actor"
            }
        }
    },
    {
        "rowkey": "0002",
        "Details": {
            "Director": {
                "Timestamp1720000000000": "Francis Ford Coppola - Updated"
            }
        },
        "Metadata": {
            "Rating": {
                "Timestamp1720000000000": "9.5"
            }
        }
    }
]

update_many("movies", updates)

scan("movies")
"""
