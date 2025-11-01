"""_summary_

Manejo de archivos (o ficheros), cómo podemos manejar ciertos archivos
a través de Python? (txt, csv, xlsx, etc)
"""

###### ---> Para archivos .txt
import os


txt_file = open("basic_code/intermediate/my_file.txt", "r+") 
# agregando a una variable, la r+ es para leer y hacer otras acciones en
# el archivo (como leer y escribir, esto se hace con el +), se cambió
# el modo a w+ que es para escribir y crear un nuevo archivo
# si queremos que se pueda leer lo que tenemos, hay que usar r+

# Vamos a hacer algo aquí: crearemos el archivo (si no lo encuentra, se crea)
## --> Escribiendo en el archivo
# txt_file.write("Hola, me llamo Fanny Gro\nTengo 28 años\nEstoy repasando Python!")

## --> Para leer archivos txt
print(f"Archivo: \n{txt_file.read()}")
# print(f"Leyendo solo un fragmento de texto:\n {txt_file.read(15)}")
# Nota con lo de arriba: si dejamos 2 reads, leera todo una vez y luego
# buscará 15 caracteres extras! Así que ojo con eso!

# print(f"Leyendo una línea del archivo: {txt_file.readline()}") # lee de linea en linea

# print(f"Leyendo líneas: {txt_file.readlines()}") # itera por el archivo e imprime las lineas

## --> Para escribir archivos txt
# txt_file.write("\nTambién puedo usar Java :D")

txt_file.close() # cerrando para no dejar el buffer abierto!

## --> Eliminando un fichero (remove), se borra el archivo de la carpeta!
# os.remove("basic_code/intermediate/my_file.txt")

###### ---> Para archivos .json, archivos muy comunes en aplicaciones web-servidor
##          es el tipo de serialización que usamos cuando se toman datos en red.
##          Es un archivo de texto que se puede usar como modelo para trabajar
##          ya sea desde el backend o en frontend. Esto podemos hacerlo con el 
##          modulo json de python.
##          Un json es mas o menos como un mapa, un diccionario, de clave-valor.
import json 

## --> Creando variable para el archivo json (OJO con el r+ y w+)
json_file = open("basic_code/intermediate/my_file.json", "r+") # buscamos y si no: creamos

## --> Ejemplo de contenido de archivo json
json_test = {
    "name" : "Fanny",
    "surname": "GM",
    "age" : 28,
    "programming" : ["Python", "Java", "JavaScript", "C#"]
}

## --> Escribiendo en el archivo json
#      dump(texto, fichero_destinado, identación), para la separacion de lineas hay 
#      varios niveles (depende de la tabulacion que queramos, usamos 4 espacios 
#      como en python). Es más que nada, para que sea más legible y comprensible
json.dump(json_test, json_file, indent= 4)

## --> Leyendo lineas del json (imprimiendo contenido)
with open("basic_code/intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

## --> Transformando json a diccionario en python
json_dict = json.load(open("basic_code/intermediate/my_file.json"))
print(json_dict)
print(type(json_dict)) # es un diccionario

###### ---> Para archivos csv
import csv

## --> Abriendo o creando archivo csv
csv_file = open("basic_code/intermediate/my_file.csv", "w+")

## --> Haciendo writer para el archivo que hemos creado
csv_writer = csv.writer(csv_file)

## --> Agregando contenido
csv_writer.writerow(["Name", "Surname", "Age", "Programming"])
csv_writer.writerow(["Fanny", "GM", 28, "Python"])
csv_writer.writerow(["Roswell", "", 2, "COBOL"])

## --> Cerramos buffer
csv_file.close()

## --> Leyendo lineas del csv (imprimiendo contenido)
with open("basic_code/intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

###### ---> Para archivos xlsx
# import xlrd # Hay que instalar el modulo, ojo! En esto quizás es mejor un venv

###### ---> Para archivos xlm
# import xml # Modulo para trabajar con xml


### NOTAS: ES POSIBLE QUE ESTO LO VEA MÁS CON LOS ELEMENTOS DE ASABENEH, CARPETA D
#          CHALLENGE_EXERCISES