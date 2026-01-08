"""Funciones para procesar elementos txt desde una url
"""
import json
import requests


# FUNCION PARA LEER TXT
def reading_txt(archive):
    """Devuelve el contenido de un archivo de texto (.txt).

    Args:
        archive (str): Ruta del archivo txt

    Returns:
        IO stream: Información del texto que se ha procesado.
    """
    with open(archive, "r", encoding="utf-8") as txt_content:
        return txt_content.read()

# FUNCIÓN PARA LEER TXT DE UNA URL
def web_reading_txt(txt):
   """Devuelve la respuesta de conexión a una url

   Args:
       txt (str): Cadena de texto que contiene la url de un texto plano.

   Returns:
       Response: Elemento de requests con la respuesta a la conexión con la web.
   """
   return requests.get(txt)

# FUNCION PARA LEER JSON
def reading_json(archive):
    text = web_reading_txt(archive).text
    json_text = json.loads(text) # cargamos el json
    return json_text