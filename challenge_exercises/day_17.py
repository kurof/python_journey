"""_summary_

Día 17 del reto Python, la lección de hoy es: Manejo de Errores!
Python hace uso del try y except (similar a try-catch en java) para
manejar errores de forma adecuada. Una salida agraciada (o un manejo
agraciado del error) es simplemente un simple idioma de programación
algo que detecta un error y se maneja de forma adecuada y controlada
como resultado.

Frecuentemente, el programa imprime un mensaje descriptivo sobre el 
error a través de la consola o un log, esto permite que nuestros 
programas sean más robustos; la causa de una excepción es usualmente
externa al programa mismo, cosas como un error de input, agregar el 
nombre incorrecto de un modulo o archivo, dispositivo IO que no fun-
ciona bien, entre otras cosas.

    Ser capaces de manejar los errores de forma adecuada evita
    que nuestro programa se detenga (crash)

La sintaxis es:

    try:
        # bloque de código que queremos ejecutar

    except: # puede tener una condición (nombre de error)
        # bloque de código en caso de que ocurra una excepción
    
    else:
        # si no hay excepciones, ejecutamos esto
    
    finally:
        # siempre se ejecuta este código!

Otra lección: packing y unpacking listas y diccionarios!
Hay dos operadores:
    - * para tuplas o listas
    - ** para diccionarios

Lo anterior lo usamos para poder pasar elementos de una estructura
de datos a una función que necesite ciertos parámetros (argumentos)
El siguiente fichero contiene ejercicios y otros trucos!
El ejercicio de esta lección se enfocará en esta última parte!

Reto original: Asabeneh
Tutoriales: MoureDev
"""

## -> Haz una lista de paises y separa los elementos en algo 
#     como "paises de latam" y almacena los otros en otras variables 
#     se hará uso de unpack y también agrega un try-except (esto es 
#     agregado por mi)
countries_names = [
    "Finlandia", "Suecia", "Noruega", "Islandia",
    "México", "Guatemala", "Nicaragua", "El Salvador",
    "Japón"
]

# Dividiendo los elementos
nordic = []
latam = []
country_one = ""

# Agregando elementos a nordic
for country in countries_names:
    nordic.append(country)

    if country == "Islandia":
        break

# recorremos otra vez la lista pero ahora desde el punto de islandia
# no es taan conveniente algo asi, pero es la mejor solucion que se 
# me ocurre...
for i in range(4, len(countries_names)):
    latam.append(countries_names[i])

    if countries_names[i] == "Japón":
        country_one = countries_names[i]
        latam.remove(countries_names[i])


print(f"Países nordicos: {nordic}")
print(f"Países latinos: {latam}")
print(f"Extra: {country_one}")