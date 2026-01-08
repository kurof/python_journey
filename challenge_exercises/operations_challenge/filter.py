"""Funciones para filtrar elementos para el archivo day_20.py,
, aquí se leerán elementos de un archivo json. Es decir, provenientes de una API
"""
from logging import info
import os
import re
from typing import Counter

from challenge_exercises.operations_challenge.txt_processing import reading_txt

# FUNCION PARA CONTAR LAS PALABRAS MÁS COMUNES
def find_most_common_words(text_or_path, n : int):
    """Encuentra las palabras más comunes en un texto o archivo.
    
    Args:
        text_or_path (str): Puede ser texto directo o ruta a archivo .txt
        n (int): Cantidad de palabras más comunes a devolver
    
    Returns:
        list: Lista de tuplas (conteo, palabra) ordenadas por frecuencia
    """
    # revisando si text_or_path es solo texto o una ruta de archivo
    if os.path.isfile(text_or_path): 
        text = reading_txt(text_or_path) # leyendo archivo
    else:
        text = text_or_path

    # haciendo la lista de tuplas (se me prendió el foco lol)
    common_words = [
        # ponemos el contador con count(word) y la palabra contada
        (text.count(word), word)
        # recorremos elementos (word) de text
        for word in set(text)
    ]

    # agregando a lista
    common_words = text.lower().split()

    # contando elementos y poniendo los más comunes
    # y regresamos las n más comunes
    return Counter(common_words).most_common(n)

# Función para filtrar raza y países de gatos
def counting_frequencies(info, search_term, n):
    json_info = [
        # Buscando el nombre del país dentro del json, si no se encuentra es NA
        (item.get(search_term, "N/A"))
        # Se recorre el contenido del json
        for item in info
        
    ]
    # Se hace el conteo de apariciones del país, es decir, cantidad de razas
    json_info = Counter(json_info).most_common(n)
    return f"\nConteo de {n} frecuencia(s): \n{json_info}"


# Función para procesar elementos que tengan un formato "1 - 2" (str) y pasarlo a numero
def rangos_str_a_numericos(info):
    just_digits = [] # TODO ver si funciona con set (opcional)

    for value in info:
        if isinstance(value, str): # si es un string
            # buscando patron "a - b" o similar
            if re.match(r"^\s*\d+(\.\d+)?\s*-\s*\d+(\.\d+)?\s*$", value):
                # se divide el string y se pasa como int a 2 variables
                d1,d2 = map(int, re.split(r"\s*-\s*", value))
                # pasando a la lista con solo numeros
                just_digits.append(d1)
                just_digits.append(d2)

    return just_digits

######## FUNCIONES ESPECIFICAS
# función para acomodar listas, especificamente para REST Countries
def sorting_population(info, n):
    # lista que toma los nombres comunes del json y el numero de poblacion
    srt_items = [
        (country.get("population", None), # obteniendo poblacion
         country.get("name", {}).get("common", "N/A")) # obteniendo nombre pais
        for country in info
    ]

    srt_items = sorted(srt_items, reverse=True) # acomodando elementos

    return srt_items[:n] # lista de tamaño n

## Función para contar los idiomas
# contando lenguaje más hablado y total de lenguajes
def counting_languages(info, n):
    raw_langs = [
        (country.get("languages", {}))
        for country in info
    ]

    langs_freq = []
    for lan_dict in raw_langs:
        for language in lan_dict:
            langs_freq.append(lan_dict.get(language))

    freqs = Counter(langs_freq).most_common(n)
    lang_count = len(set(langs_freq))

    return f"Total idiomas: {lang_count} \n{n} más hablados: {freqs}"

# Función para extraer elementos del json
def extracting_cat_numeric_data(txt, search_term):
    # normalizando termino de busqueda 
    search_term = search_term.lower()
    # diccionario para guardar los elementos
    cat_info = []
    for cat in txt:
        # se obtienen los valores del termino de busqueda
        if search_term == "weight":
            value = cat.get(search_term, {}).get("metric", None)
        elif search_term == "life_span":
            value = cat.get(search_term, None)
        else:
            value = cat.get(search_term, "N/A")

        # agregando el registro al diccionario
        # cat_info.append({
        #     search_term : value
        # })
        cat_info.append(value) # pasando solo los valores, no el apartado
        
    # se limpia el formato para que solo sean los numeros (si es necesario)
    cat_info = rangos_str_a_numericos(cat_info)
    return cat_info

