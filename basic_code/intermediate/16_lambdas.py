"""
La lección de hoy es lambda!
El concepto de una lambda podemos entenderlo como una función, pero
tienen la peculiaridad de ser funciones anónimas, es decir, no tendrán
un nombre (como cuándo hacemos un def nombre_funcion()) ni tampoco
la palabra reservada def.

Para crear una función lambda, hacemos uso de su palabra reservada:
lambda. Pueden tener parámetros de entrada, además, es posible 
almacenarla en una variable para su uso!

    - Es muy útil para simplificar y ahorrar tiempo con ciertas operaciones

Un buen uso de las lambdas es si solo se usan dentro de un fichero/
archivo y no necesitamos que su operación salga del fichero a otra parte del
programa.
Como nota adicional: es posible agregar lambdas a una función!
"""

## Haciendo una función lambda que suma 2 números
sum_values = lambda first_value, second_value : first_value + second_value
print(sum_values(5,5)) # llamando lambda

# creando otra lambda que mutiplique valores
multiply_values = lambda value1, value2 : print(f"Multiplicación: {value1 * value2 + 2}")
multiply_values(2,3) # llamando lambda

# metiendo lambda a una función existente
def sumando_valores(value1):
    return lambda value2, value3 : value1 + value2 + value3

# llamando a funcion con lambda (parametro_funcion)(parametros_lambda)
print(f"Funcion con lambda: {sumando_valores(2)(4,5)}")