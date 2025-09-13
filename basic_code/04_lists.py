"""_summary_
Esta es la primera estructura de datos que estamos viendo ahora!
Es decir, nos ayuda a acomodar varios datos, tendría una ligera 
similitud con los arrays pero son más avanzadas y hasta tienen
una palabra reservada: list() o usar []

Una entidad, un objeto y no olvidemos que Python es un POO.

La lista nos proporciona operaciones propias de esta clase, 
como agregar elementos, ordenar, eliminar, etc. Python NO
tiene arrays.

-- Es posible agregar elementos duplicados en una lista

Tutoriales: MoureDev
"""

# --> Declarando listas
my_list = list()
my_other_list = []

my_list = [35, 24, 28, 62, 52, 30, 30, 17] # agregando elementos
my_other_list = [28, 1.63, "Fanny", "GM"] # agregando diferentes datos

# --> Imprimiendo listas y sacando otros datos de ellas
print(len(my_list))
print(f"Lista: {my_other_list} \nTipo: {type(my_other_list)}")

# --> Accediendo a elementos en la lista
print(f"Primer elemento: {my_other_list[0]}")
print(f"Segundo elemento: {my_other_list[1]}")
print(f"Último elemento: {my_other_list[-1]}")
print(f"Elemento sorpresa -3: {my_other_list[-3]}")

print(f"¿Cuántas veces aparecen \"Fanny\"? {my_other_list.count("Fanny")}")

# --> Asignando variables a my_other_list
# Hay que agregarlas acorde al orden
# age, height, name, surname = my_other_list 
age, height, *rest = my_other_list# se puede hacer esto :0
print(f"\nAccediendo a elemento \"name\": {rest}")

# --> Concatenando listas
print(my_list + my_other_list)

# --> Agregando elementos a la lista
my_other_list.append("kurof")
print(my_other_list)

my_other_list.insert(1, "Rosa") # agrega valor en un posicion especifica
print(my_other_list)

my_other_list[1] = "Verde" # reescribiendo el valor
print(f"Lista editada: {my_other_list}")

# --> Eliminando elementos de una lista
my_other_list.remove("Verde")
print(f"Eliminando color Verde: {my_other_list}")

# usando la otra lista y eliminando elementos en posiciones especificas (pop)
my_list.remove(30)
print(my_list)

my_list.pop() # esto nos puede devolver el elemento eliminado
print(f"Quitando el ultimo elemento (default): {my_list}")
print(my_list.pop(2)) # quitando el 3er elemento

# --> BORRANDO elementos de la lista
del my_list[2] # borrar completamente el 3er elemento
print(my_list)

# --> Copiando una lista
my_new_list = my_list.copy()
print(f"Copia de la lista: {my_new_list}")
my_new_list.reverse()
print(f"Invirtiendo el orden: {my_new_list}")
my_new_list.sort()
print(f"Lista ordenada: {my_new_list}")

# --> BORRAR TODOS LOS ELEMENTOS DE LA LISTA
my_list.clear()
print(my_list)