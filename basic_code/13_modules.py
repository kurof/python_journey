"""__summary__

La siguiente lección son: modulos, que son elementos que
cumplen una función específica. Es una librería dónde tenemos
código, nuestros archivos/ficheros que hemos hecho hasta ahora
pueden funcionar como modulos! Y esto lo hacemos con la 
palabra reservada: "import", seguido del nombre del fichero.

    Importante: al momento de importar el modulo, si queremos
    hacer uso de las funciones dentro de este, hay que llamar
    primero al modulo y luego ponemos un punto para ver lo que
    hay (ej: modulo_nombre.funcion())

    Otra cosa importante: hay que usar ficheros que tengan una
    nomenclatura/sintaxis válida! Un modulo no tiene números
    al principio (tampoco es recomendable usar palabras reservadas
    como nombre, no sé si se haga algo similar al override aquí)
    También es bueno usar nombres que tengan cierta descripción
    de su función

Los módulos nos ayudan a hacer una aplicación escalable,
segura; y no solo podemos usar modulos que hagamos nostros, 
si no que podemos usar modulos que otros hagan (el que se me
viene a la mente es: random, para generar numeros aleatorios).
También podemos usar elementos que vienen del sistema de Python!
"""

# importando un modulo de ejemplo (dentro de nuestro proyecto)
# import example_module

# si queremos importar una sola función / método:
from example_module import print_element, suma_valores
# modulo del sistema
import math
from random import randint as num_aleatorio # podemos darle alias

# example_module.suma_valores(10,5,5)
# example_module.print_element("Hola :D")

# si importamos solo las funciones
suma_valores(10,5,5) # wow!
print_element("Solo importe mi función!")

# usando modulo del sistema
print(f"Pi: {math.pi}")
print(f"Numero random entre 1 y 10: {num_aleatorio(1,10)}")