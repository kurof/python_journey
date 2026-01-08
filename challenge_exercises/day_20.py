"""_summary_

Día 20 del reto Python: manejo de paquetes en Python (Python Package Manager).

¿Qué es PIP? PIP es, es español, un Programa Instalador de Preferidos; lo 
usamos para instalar diferentes paquetes dentro de nuestro entorno Python.
Un paquete puede contener uno o más modulos, incluso hasta otros paquetes! En
la programación, no es necesario tener que escribir cada programa de utilidad,
si no que instalamos paquetes que nos ahorren ese trabajo y los importamos a 
nuestro proyecto.

Algunos ejemplos de paquetes más populares en Python:

    1. SQLAlchemy o SQLObject, para bases de datos, nos da un acceso orientado
       a objetos a muchos sistemas de bases de datos.
    2. Django, para desarrollo web, un framework de alto nivel.
    3. Flask, para desarrollo web, microframework más simple que Django.
    4. Beautiful Soup, parser HTML, diseñado para proyectos rápidos como screen-
       scraping para obtener datos de páginas web.
    5. PyQuery, implementa jQuery en Python, se dice que es más rápido que 
       Beautiful Soup :D
    6. ElementTree, procesamiento de XML, un tipo Element es un objeto contenedor
       bastante flexible, diseñado para almacenar datos estructurados (infosets XML)
       en memoria.
         Dato adicional -> Esto está implementado en la librería estandar desde la 
         versión 2.5
    7. PyQt, GUI, son elementos necesarios para construir cross-platforms con el 
       framework Qt.
    8. TkInter, GUI, son las herramientas tradicionales para crear interfaces gráficas
       en Python.
    9. Numpy, numeric python, es una de las herramientas más populares en machine
       learning.
   10. Pandas, es una librería tanto para data science, data analysis y machine learning
       que provee estructuras de datos de alto nivel y amplia variedad de herramientas
       para su análisis.
   11. request, para red/web, es un paquete que podemos usar para enviar requests a un
       servidor (GET, POST, PUT, DELETE)
   
   Y muchos más!

   Fuera de eso, sé que esto será adelantado a las lecciones pero para evitar conflictos,
   voy a hacer uso de un entorno virtual para la instalación de elementos!
      Nota importante: LEER BIEN LAS RUTAS DEL VENV

Reto original: Asabeneh
Tutoriales: MoureDev
"""
################ EJERCICIOS
## --> Lee la url proporcionada abajo (romeo_and_juliet) y encuentra las 10 palabras
#      más comunes
from collections import Counter
import os
from challenge_exercises.operations_challenge.filter import counting_frequencies, counting_languages, extracting_cat_numeric_data, sorting_population
from challenge_exercises.operations_challenge.operaciones import info_mean, info_median, info_standard_dev, maximum_value, minimum_value
from challenge_exercises.operations_challenge.txt_processing import reading_json

# from challenge_exercises.operations_challenge.operaciones import info_mean, info_median, info_standard_dev, maximum_value, minimum_value
# from .operations_challenge.filter import counting_frequencies, extracting_cat_numeric_data, find_most_common_words
# from .operations_challenge.txt_processing import reading_json, web_reading_txt

#### --> Llamando a las funciones
## -> PRIMER EJERCICIO
# romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
# rj_response = web_reading_txt(romeo_and_juliet)
# text = rj_response.text

# print(type(rj_response))
# print(f"Palabras más comunes: \n{find_most_common_words(text, 10)}")

## -> SEGUNDO EJERCICIO
## --> Lee la API de gatos y busca el min, max, promedio, mediana y standard deviation
#      de el peso y luego de la esperanza de vida; luego crea una tabla de frecuencias
# #      con los países y la raza de gato
# cats_api = "https://api.thecatapi.com/v1/breeds"
# cats_api = reading_json(cats_api)

# info_weight = extracting_cat_numeric_data(cats_api, "weight")

# print("-- Operaciones con la información (WEIGHT) --")
# print(minimum_value(info_weight))
# print(maximum_value(info_weight))
# print(info_mean(info_weight))
# print(info_median(info_weight))
# print(info_standard_dev(info_weight))

# info_ls = extracting_cat_numeric_data(cats_api, "life_span")
# print("\n-- Operaciones con la información (LIFE_SPAN)--")
# print(minimum_value(info_ls))
# print(maximum_value(info_ls))
# print(info_mean(info_ls))
# print(info_median(info_ls))
# print(info_standard_dev(info_ls))

# print(counting_frequencies(cats_api, "origin", 10))

## --> EJERCICIO 3
#  Lee la API de countries y encuentra los 10 países más poblados,
#  los 10 lenguajes más hablados y el total de lenguajes hablados
# Nota: la API original del ejercicio se ha pasado a algo de paga, así que
# uso restcountries v3 (es necesario poner los elementos para no dar error)
countries_info = "https://restcountries.com/v3.1/all?fields=name,population"
countries_info = reading_json(countries_info)

countries_lang = "https://restcountries.com/v3.1/all?fields=name,languages"
countries_lang = reading_json(countries_lang)

# print(sorting_population(countries_info, 10))
# print(type(countries_info))
# print(countries_lang)
print(counting_languages(countries_lang, 10))
# print(counting_frequencies(countries_lang, "languages",10))

# TODO hacer la función que me ayude a filtrar esto ^
# TODO 2 -> Ver qué operaciones se pueden hacer en una lista