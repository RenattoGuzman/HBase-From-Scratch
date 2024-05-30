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

# 1. Listar tablas
# list_table()

# 2. Crear tabla sin column_families

#column_families = []
# create("prueba1", column_families)

# 3. Crear tabla con una column_family

#column_families = ["CF1"]
# create("prueba1", column_families)

# 4. Listar tablas
# list_table()

# 5. Crear tabla con tres column_family

# column_families = ["CF1", "CF2", "CF3"]
# create("prueba2", column_families)

# 6. Describe prueba2
# describe_table("prueba2")

# 7. Listar tablas
# list_table()

# 8. Insertar un registro a CF1, CF2, CF3

# put("prueba2", "0001", "CF1", "CQ1", "valor1")
# put("prueba2", "0001", "CF2", "CQ2", "valor2")
# put("prueba2", "0001", "CF3", "CQ3", "valor3")

# 9. Actualizar Celda CF2

# put("prueba2", "0001", "CF2", "CQ2", "nuevo_valor1")

# 10. Actualizar la celda de "prueba2" CF2 otra vez

# put("prueba2", "0001", "CF2", "CQ2", "nuevo_valor2")

# 11. Actualizar la celda de "prueba2" CF2 otra vez

# put("prueba2", "0001", "CF2", "CQ2", "nuevo_valor3")

# 12. Mostrar los cambios en el archivo de la tabla, con las 3 versiones de la celda
# get("prueba2", "0001", "CF2", "CQ2")

# 13. Revisar is enable prueba2
# is_enabled("prueba2")

# 14. Desactivar tabla 2
# disable('prueba2')

# 15. Insertar solo un valor CQ (NO DEBE PERMITIR)

"""""
table = "prueba2"
row_key = "XASXS"
family = "dSXSA"
qualifier = "OCHOA"
value = "CQ"

put(table, row_key, family, qualifier, value)
"""""

# 16. Revisar is disabled

# is_enabled("prueba2")

# 17. Deshabilitar "prueba2" 
# disable("prueba2")

# 18. Habilitar "prueba2"
# enabled("prueba2")

# 19. Habilitar "prueba2" (indicar que ya esta habilitada)
# enabled("prueba2")

# 20. Insertar un registro en "prueba2" con un valor en un CQ unicamente

# put("prueba2", "0002", "CF1", "CQ1", "valor5")

# 21. Insertar un registro en "prueba1" con un valor en un CQ unicamente

# put("prueba1", "0001", "CF1", "CQ1", "valor1")

# 22. Obtener primer registro de "prueba2" sin especificar CF ni CQ en formato legible

"""""
table = "prueba2"
row_key = "0001"
family = ""
qualifier = ""
timestamp = ""

get(table, row_key, family, qualifier, timestamp)
"""""

# 23. Obtener primer registro de "prueba2" con CF especificado en formato legible
"""""
table = "prueba2"
row_key = "0001"
family = "CF1"
qualifier = ""
timestamp = ""

get(table, row_key, family, qualifier, timestamp)
"""""

# 24. Obtener primer registro de "prueba2" con CF:CQ especificados en formato legible
"""""
table = "prueba2"
row_key = "0001"
family = "CF1"
qualifier = "CQ1"
timestamp = ""

get(table, row_key, family, qualifier, timestamp)
"""""

# 25. Obtener primer registro de "prueba2" con CF:CQ y version especificados en formato legible
"""""
table = "prueba2"
row_key = "0001"
family = "CF3"
qualifier = "CQ3"
timestamp = "Timestamp1717047936412"

get(table, row_key, family, qualifier)
"""""

# 26. Scan de "prueba2" en formato legible
# scan("prueba2")

# 27. Scan de tabla grande en formato legible
# scan("tabla_grande")

# 28. Alter "prueba2" agregar CF4
# alter_table("prueba2", ["CF4"])

# 29. Alter "prueba2" modificar CF4

# alter_table("prueba2", ["CF4"])

# 30. Deshabilitar "prueba2"
# disable("prueba2")

# 31. Alter "prueba2" eliminar CF4
# alter_table("prueba2", [])

# 32. Habilitar "prueba2"
# enabled("prueba2")

# 33. Alter "prueba2" eliminar CF4
# alter_table("prueba2", [])

# 34. Count "prueba2"
# count("prueba2")

# 35. Count de tabla grande
# count("tabla_grande")

# 36. Truncate a una de las tablas pequeñas precargadas
# truncate("shows")

# 37. Deshabilitar la otra tabla pequeña precargada
# disable("movies")

# 38. Truncate de la tabla pequeña deshabilitada
# truncate("movies")

# 39. Delete del registro de "prueba1"
# delete_all("prueba1", "0001")

# 40. Deshabilitar "prueba2"
# disable("prueba2")

# 41. Delete del segundo registro de "prueba2"
# delete_all("prueba2", "0002")

# 42. Habilitar "prueba2"
# enabled("prueba2")

# 43. Delete all "prueba2"
# delete_all("prueba2", "0001")
# delete_all("prueba2", "0002")

# 44. Insertar un registro en "prueba2" con un valor de CQ en cada CF
# put("prueba2", "0001", "CF1", "CQ1", "valor1")
# put("prueba2", "0001", "CF2", "CQ2", "valor2")
# put("prueba2", "0001", "CF3", "CQ3", "valor3")

# 45. Deshabilitar "prueba2"
# disable("prueba2")

# 46. Delete all de "prueba2"
# delete_all("prueba2", "0001")

# 47. Habilitar "prueba2"
# enabled("prueba2")

# 48. Drop de la tabla pequeña precargada que está deshabilitada
# drop_table("movies")

# 49. Drop de "prueba2"
# drop_table("prueba2")

# 50. Drop all
# drop_all_tables()

####################################################### Otras pruebas que hicimos #######################################################

## COUNT
# count("shows")

## SCAN
# scan("movies")

## DROP TABLE
# drop_table("movies")
# DROP ALL
# drop_all_tables()

"""
table = "movies"
row_key = "0001"
family = "Cast"
qualifier = "Actor"
value = "Renatto Guzman"
"""


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
