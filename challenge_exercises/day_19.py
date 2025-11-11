"""_summary_

Día 19 del reto Python, la lección de hoy es: Manejo de Archivos!
Usualmente almacenamos datos en archivos con diferentes tipos de formato,
archivos como: .txt, .json, .xml, .csv, .tsv, excel, etc.

Manejar archivos es un aspecto importante de la programación en dónde 
podemos crear, leer, actualizar y borrar archivos. 

    - open("nombre o ruta del archivo", modo) -> para abrir archivos, el
      modo se refiere a qué acciones se harán sobre el archivo:
        - "r" (read only), valor por default, indica que se abre el archivo para solo
          lectura (si no existe, devuelve un error).
        - "a" (append), abre archivo solo para agregar al final del archivo (crea el archivo si
          no existe).
        - "w" (write only), se abre el archivo para escritura / edición (se crea el 
          archivo si no existe).
        - "x" (create), crea específicamente un archivo (devuelve error si ya existe).
        - "t" (text), valor predeterminado, es un modo de texto.
        - "b" (binary), modo binario (se puede usar con imágenes)

    - close() -> para cerrar el buffer del sistema que abre el archivo, siempre se 
      recomienda cerrar cada vez que abrimos un archivo.
      Aunque esto se puede hacer de forma automática con el método with, dejando:
            with <ruta de archivo> as <variable>:
                # acciones

Para borrar archivos existentes usamos remove de os, una librería que hay que importar
si queremos hacer uso de este método.

También, cada tipo de archivo puede tener diferentes métodos de edición!

El siguiente fichero contiene mi solución a los ejercicios de la lección del día!

Reto original: Asabeneh
Tutoriales: MoureDev
"""
###### --> EJERCICIOS DE NIVEL 1
## --> Escribe una función que cuente el número de líneas y el número de palabras en
#      un texto. Los archivos están en la carpeta de este reto (los discursos de varios
#      presidentes de USA y sus primeras damas), lo que hay que hacer es:
#           - Lee los archivos y cuenta los números de líneas y palabras

# importaciones
from collections import Counter
import json
import re

# Haciendo función para contar palabras
def count_and_read(archive_path):
    """Devuelve un conteo de palabras de un archivo de texto.

    Args:
        archive_path (str): Ruta del archivo a procesar

    Returns:
        int: Conteo total de palabras (elementos de la lista del texto)
    """
    # variables
    word_count = 0

    # abriendo archivo
    with open(archive_path) as a: # abriendo el archivo con la ruta
        texto = a.read().strip("\"\n\"").split() # quitamos elementos \n y dividimos por espacio

    with open(archive_path) as a:
        text_lines = a.readlines() # lista con las lineas del txt
        for line in text_lines: 
            # buscamos los elementos que solo tengan \n
            if line == "\n":
                text_lines.remove(line)
        # print(text_lines)
    
    # contador de lineas
    line_count = len(text_lines)

    # recorriendo lista de palabras
    for word in texto:
        # si hay un elemento de tipo guión
        if word == "-" or word == "–":
            continue # saltamos
        word_count += 1 # sumamos +1 palabra

    return f"Total de palabras: {word_count} & número de líneas: {line_count}"
        
print(f"Obama's speech -> {count_and_read("challenge_exercises/obama_speech.txt")}")
print(f"Michelle's speech -> {count_and_read("challenge_exercises/michelle_obama_speech.txt")}")
print(f"D Trump's speech -> {count_and_read("challenge_exercises/donald_speech.txt")}")
print(f"Melania T's speech -> {count_and_read("challenge_exercises/melina_trump_speech.txt")}")


## --> Lee el archivo de countries_data.json en el directorio, crea una función que 
#      encuentre los 10 lenguajes más hablados
def json_to_dict(archive):
    """Lee un archivo json y lo convierte a un diccionario.

    Args:
        archive (str): Ruta del archivo json

    Returns:
        dict/list: Devuelve una lista de diccionarios
    """
    with open(archive, "r", encoding="utf-8") as jt:
        return json.load(jt)


def most_spoken_languages(archive_path: str, top : int):
    """Devuelve la cuenta de los idiomas más hablados en un archivo json.

    Args:
        archive_path (str): Ruta del archivo json
        top (int): Cantidad de elementos que buscamos mostrar

    Returns:
        Counter: Lista de elementos collections.Counter con el contador y elemento
    """
    # leyendo json
    json_content = json_to_dict(archive_path)

    # procesando la lista de diccionarios
    languages = []
    # recorriendo la lista inicial json_content
    for country in json_content:
        languages.extend(country.get("languages", []))
    
    # contando lenguajes
    langs_count = Counter(languages)

    # usamos el método most_common de collections para
    # regresar los n más frecuentes
    return f"Top {top} de lenguajes más comunes: \n{langs_count.most_common(top)}"


## --> Lee el archivo de countries_data.json y crea una función que devuelva los 
#      10 países más poblados
def most_populated_countries(archive_path: str, top : int):
    """Devuelve una lista de diccionarios ordenada de forma ascendente sobre los 
    países más poblados de un archivo json.

    Args:
        archive_path (str): Ruta del archivo json
        top (int): Número de elementos que se mostrarán de la lista

    Returns:
        list : Lista de elementos ordenados hasta "top"
    """
    # leyendo json
    json_content = json_to_dict(archive_path)

    # procesando la lista de diccionarios (lista de diccionarios)
    people_count = [
        # tomando keys y valores gracias a get
        {"country" : country.get("name"), 
         "population" : country.get("population",0)}
        # recorriendo el contenido original
        for country in json_content
    ]

    # acomodando elementos, dentro de nuestra lista de diccionarios
    # resultante, vemos entre la key de población: si es más grande que
    # la anterior, la pasamos arriba
    people_count = sorted(people_count, key= lambda x: x["population"], reverse= True)
    
    return people_count[:top] # imprimimos solo hasta el limite de top

json_path = "challenge_exercises/countries_data.json"
print(most_spoken_languages(json_path, 3))
# print(f"\n{most_populated_countries(json_path, 10)}")

# imprimiendo línea por línea
print("\nPaíses más poblados: ")
populated_countries = most_populated_countries(json_path, 10)
for country_line in populated_countries:
    print(country_line)


###### --> EJERCICIOS DE NIVEL 2
## --> Extrae todos las direcciones de email del archivo email_exchange_big.txt
# para leer el archivo
def reading_txt(archive):
    with open(archive, "r", encoding="utf-8") as txt_content:
        return txt_content.read()
    
def extracting_emails(archive_path):
    # leyendo texto
    content = reading_txt(archive_path)

    # regex para encontrar los emails
    # patrón: cualquier caracter alfanumérico + @ 
    # + cualquier caracter alfanumérico + . + 2 o más letras
    # esto se guarda en una lista (esto se hizo con ayuda de copilot)
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

    return emails

txt_path = "challenge_exercises/email_exchanges_big.txt"
print(extracting_emails(txt_path))