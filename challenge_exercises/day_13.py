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
# tuple_list1 = [(i*0 if i != 1 else 1, 1) for i in range(8)]
# tuple_list2 = [(i*2 if i != 1 else i-2,2) for i in range(8)] # pendiente

# otra forma de hacerlo... no sé si funcione (partiendo del 0 al 11, para que sea 10)
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) 
              for i in range(0,11)] 

# imprimiendo las tuplas! Y si funcionó!
for i in tuple_list:
    print(i)

# print(tuple_list)
# print(tuple_list_final)

### --> Encongiendo una lista de elementos a otra
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

# # quitando un nivel de la lista y dejando las tuplas
# new_list = [(country, city) for sublist in countries for (country, city) in sublist]

# pasando las tuplas a una lista
# new_list = [list(country, city) for sublist in countries for (country, city) in sublist]
new_list = [list(country_city) for sublist in countries for country_city in sublist]

# agregando elementos...?
print(new_list[0].index("Helsinki")) # para ver como funciona

# agregando "FIN", "SWE", "NOR"
new_list[0].insert(1, "FIN")
new_list[1].insert(1, "SWE")
new_list[2].insert(1, "NOR")
print(new_list)

## transformando la lista de countries a un diccionario
new_dict = [{"country":country, "city": city} 
                 for sublist in countries 
                 for country, city in sublist]
print(new_dict)

## transformando una lista a una lista de textos concatenados
names = [[("Agatha", "Surana")], [("Garreth", "Hawke")], [("Vitani", "Lavellan")]]
new_string_list = [f"{first} {last}" for sublist in names for (first, last) in sublist]

print(f"Lista string: \n{new_string_list}")

## usando lambda para resolver una interesección en el eje y
# formula -> m = (y2 - y1)/(x2 - x1)
slope = lambda y1, y2, x1, x2 : round((y2 - y1) / (x2 - x1),2)
print(f"Pendiente: {slope(5,10,7,15)}")