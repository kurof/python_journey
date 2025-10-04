"""_summary_

Día 12 del Reto de Python! La lección es: Modulos (Modules).
Un módulo es un archivo que contiene un conjunto de códigos o
funciones que pueden ser usadas dentro de una aplicación. Un
módulo puede ser un archivo con una sola variable, una función
o un código extenso.

Esto me recuerda bastante a los paquetes / librerías en otros
lenguajes como Java.
Para crear un modulo, escribimos el código un archivo .py y lo
guardamos dentro de nuestro proyecto ya sea en la misma carpeta
o en otra carpeta. Para usar el modulo, hacemos uso de la 
palabra reservada "import" seguido del nombre de nuestro módulo.
"""

# importando funciones de un modulo original
from random_id import random_user_id, user_id_gen_by_user
from color_gen import list_of_hexa_colors, rgb_color_gen

# generando IDs
print(f"Generando id de 10 caracteres: {random_user_id(10)}")

chars = int(input("Caracteres para tu usuario: "))
cantidad_ids = int(input("IDs que quieres generar: "))
print(f"IDs generados: \n{user_id_gen_by_user(chars, cantidad_ids)}")

# generando colores
rgb_color_gen()
print(f"Lista de hexadecimales: \n{list_of_hexa_colors(4)}")