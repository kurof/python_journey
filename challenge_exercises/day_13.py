"""__summary__

Día 13 del reto Python, el tema de hoy es: List Comprehension, o
comprensión de listas y uso de lambdas!
La comprensión de listas en Python es hacer una forma compacta de
crear una lista a partir de una secuencia; es considerablemente más
rápido que procesar una lista de forma convencional con un loop for.

Sintaxis:
    i for i in iterable if expression

    - Donde la parte del if puede ser opcional

Ahora, ¿qué es una lambda? es una función "anónima", sin nombre. 
Puede tomar varios argumentos pero solo puede ser una expresión!
Podemos usarlas dentro de otras funciones también!

Sintaxis:
    x = lambda param1, param2, param3, ... = <operacion con parametros>

"""

#### ----> Ejercicios

# Filtremos solo el 0 y los numerso negativos
numbers = [-4,-3,-2,-1,0,2,4,6]
filtered_numbers = [i for i in numbers if i <= 0]
print(f"Lista con 0 y negativos: {filtered_numbers}")

# Haciendo una lista de una sola dimension
list_of_lists = [[[1,2,3], [4,5,6], [7,8,9]]]
list_one_d = [num for row in list_of_lists for num in row]
print(f"Lista 1 dimension: {list_one_d}")

# Haciendo una lista de tuplas??
# og_list = [0,1,0,0,0,0,0]
tuple_list1 = [(i*0 if i != 1 else 1, 1) for i in range(8)]
tuple_list2 = [(i*2 if i != 1 else i-2,2) for i in range(8)] # pendiente

print(tuple_list2)
# print(tuple_list_final)