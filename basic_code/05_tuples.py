"""_summary_
Una tupla es un conjunto de valores; si bien tiene elementos
parecidos a las listas, una tupla se diferencia, de entrada, 
con sus definiciones dónde se usan los paréntesis o la palabra
reservada tuple(); tampoco se pueden usar las mismas funciones
que en las listas y, más importante: ES INMUTABLE, no se puede
alterar el contenido de una tupla, se pueden poner valores 
repetidos, pero no se puede alterar el contenido o agregar
contenido.

    - La tupla es usada preferentemente si queremos valores
      constantes, tal cuál
    - Si se quiere cambiar algo dentro de la tupla, lo mejor
      es cambiarlo a una lista

Tutoriales: MoureDev
"""

# --> Definiendo una tupla
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (28, 1.63, "Fanny", "GM")
my_other_tuple = (35, 30, 28)

print(f"Mi tupla: {my_tuple} \nTipo: {type(my_tuple)}")

# --> Usando algunas funciones en la tupla
print(f"\"Fanny\" aparece: {my_tuple.count("Fanny")} vez/veces")
print(f"Índice de \"GM\": {my_tuple.index("GM")}")

# --> Concatenando tuplas
combined_tuple = my_tuple + my_other_tuple
print(f"\nCombinación de tuplas: {combined_tuple}")

# --> Partiendo la tupla
print(f"\Extrayendo elementos: {combined_tuple[3:6]}")

# --> Reasignando la tupla
my_tuple = list(my_tuple)
print(f"Nuevo tipo de la tupla: {type(my_tuple)}")

# --> Borrar toda la tupla
del my_tuple