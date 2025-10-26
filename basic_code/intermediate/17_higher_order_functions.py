"""
 --- La siguiente lección son: Funciones de Orden Superior!
 Una función de este tipo hacen cosas dentro de otras funciones, digamos
 que son aquellas funciones que están en lo más alto de la jerarquía.
 
 Funciones dentro de funciones y que pueden usarse sin problema, incluso
 el mismo sistema los tiene!
 En pocas palabras -> funciones que llaman a otras funciones.

    Nota: este tipo de funciones están en todos los lenguajes!

 --- Otro concepto a ver: Closures!
 Dentro del mismo tema de funciones de orden superior; estas son funciones
 en las que podemos hacer otras funciones que cumplan con cierta tarea,
 me suena a funciones anidadas la verdad.
 Son funciones que ejecutan otro bloque de código que pertenece a otra
 función dentro de la misma y nos retorna una función.
 Sintaxis:

    def first_function(parameter1, ...):
        def sec_function(parameter1, parameter2,...):
            # bloque de codigo a ejecutar

        return sec_function

    - Para usar las instrucciones de adentro, guardamos en una variable
    - También podemos llamarlo como function_principal(param_principal)(param_sec)
"""
##### ----> Funciones de orden superior
from functools import reduce
from typing import override


print("--- FUNCIONES DE ORDEN SUPERIOR ---")
# hagamos otra (si, es un poco revuelto)
def sum_one (value):
    return value + 1 # relacionado a la funcion de abajo!

def sum_five(value):
    return value + 5

# empezamos creando una función
# def sum_two_values_plus_one(value1, value2):
#     # return value1 + value2
#     #en lugar de usar lo de arriba ^, llamamos a la otra funcion:
#     return sum_one(value1+value2) # podemos poner una operacion!

# # así, solo es necesario agregar los argumentos de una sola funcion
# print(f"Resultado función de orden superior: {sum_two_values_plus_one(5,2)}")

# otra forma de hacerlo: pasando la funcion como parametro
def sum_values(value1, value2, f_sum):
    # llamando a la función sum_one
    return f_sum(value1 + value2)

print(f"Usando función como parámetro (sum 1): {sum_values(5,2,sum_one)}")
print(f"Usando función como parámetro (sum 5): {sum_values(5,2,sum_five)}")

### ---> Closures!
print("\n--- Usando CLOSURES ---")
def sum_ten(principal_value):
    # funcion dentro de funcion vv
    def adding(value):
        return value + 10 + principal_value# sumando
    return adding # regresamos la funcion!

# usando una variable para la funcion (y agregando un parametro)
closure_function = sum_ten(10)
print(f"Usando variable y closure: {closure_function(5)}")

# otra forma de llamar! creo que está es menos engorrosa <3
print(f"Usando otra forma de llamar a closure: {sum_ten(10)(5)}")

### Funciones built-in (del sistema pue) de orden superior
print("\n--- Usando FUNCIONES BUILT IN ---")

# Map -> trabaja con iteraciones, es decir, estructuras de datos
#        y debemos especificar qué vamos a hacer con ello
print("---> Usando Map")
numbers = [2,4,6,8,10,12,14,16,18,20]

# hagamos una funcion que multiplique esto por 3
def multiply_by_three(number):
    return number * 3

# llamando a map y agregando a una lista para que nos muestre resultados
print(f"Usando map para iterar una lista: \n{list(map(multiply_by_three, numbers))}")

# también podemos meterle lambdas!
print(f"Usando map combinado con una lambda: \n{list(
    map(lambda number: number * 3, numbers)
)}")

# Filter -> funcion también con iteraciones y podemos agregar ciertos
#           criterios
print("---> Usando Filter")

# creamos una funcion
def greater_than(num):
    # procesando
    if num > 10:
        return True
    return False

# usando filter
print(f"Usando Filter: {list(filter(greater_than, numbers))}")
# con lambda (más rápido que lo de arriba)
print(f"Filter con lambda: {list(filter(
    lambda number : number >= 10, numbers
))}")

# Reduce -> como todas las funciones del sistema, necesita un iterador,
#           un elemento que sea iterable (como una lista, por ejemplo).
#           Opera entre los valores que va a recorrer. Es como un tipo
#           de sumatoria.
#           Como nota curiosa, esta función si se importa, no como las
#           anteriores.

# haciendo funcion
def sum_more_values(value1, value2):
    return value1 + value2

# usando la misma lista de numeros
print(f"Usando reduce: {reduce(sum_more_values, numbers)}")