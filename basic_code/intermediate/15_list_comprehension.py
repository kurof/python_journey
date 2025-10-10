"""__summary__

La lección de hoy es: List Comprehension, o comprensión de listas!
Hay una forma de hacer una lista de forma comprimida, rápida o 
en base a listas que ya existan en nuestro código!
Es un mecanismo bastante potente que nos puede ayudar a hacer 
listas de forma rápida, esto gracias al ciclo que podemos agregar

Sintaxis:

    i for i in <element or range>

    Donde i es declarado y usado en la misma linea:
        i = 0
        for i in ...

En pocas palabras, estamos modificando una lista desde el momento
en el que la estamos declarando :0
"""

# haciendo una lista (original)
og_list = [0,1,2,3,4,5,6,7,8,9]

# haciendo otra lista de forma resumida!
my_new_list = [i for i in og_list] 
print(f"Lista original: {og_list}")
print(f"Lista nueva con list comprehension: {my_new_list}")

# haciendo una lista a base de otra
my_range= range(1,6)
list_w_range = [i for i in my_range]
print(list_w_range)

# la primera i será el tipo de elemento que queremos guardar,
# por ejemplo, si quisieramos que se pusieran elementos n*2,
# a partir de una lista existente (es decir, multiplicando
# cada elemento por 2)
list_multiplied = [i*2 for i in og_list]
print(f"Lista multiplicada por 2 -> {list_multiplied}")

# usando una funcion
def adding_five(n):
    return n + 5

# aplicando funcion a una lista
list_w_function = [adding_five(i) for i in range(8)]
print(f"Lista con función: {list_w_function}")