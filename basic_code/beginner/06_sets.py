"""_summary_

Un set podrá parecer similar a una lista o una tupla pero
hay algunas diferencias, por ejemplo:

    - NO es una estructura ordenada, por lo que no habrá
      mucho control sobre los elementos.
    - NO admite repeticiones
    - NO garantiza orden en los datos

    - SE ACOMODA DE FORMA ALEATORIA!!!!!!

    - La palabra reservada set()
    - Podemos usar llaves {} pero también podemos usarlos 
      para declarar diccionarios! Pero se identifica al 
      momento de agregar datos
    
"""

my_set = set() # <- clase de tipo: set
my_other_set = {} # inicialmente dirá que es un diccionario

my_other_set = {"Fanny", "GM", 28} # agregando elementos

print(f"Tipo -> {type(my_other_set)}") # WOW! se hace un set

# Usando operaciones del sistema
print(f"Tamaño: {len(my_other_set)}")
# del my_other_set # borrando el set entero!

# Usando operaciones para sets
my_other_set.add("On Python journey")
print(f"Lista con nuevo elemento: {my_other_set}")

print(f"Está el elemento \"Fanny\": {"Fanny" in my_other_set}") # encontrando un elemento

my_other_set.remove("GM")
print(f"Lista sin \"GM\": {my_other_set}")

# my_other_set.clear() # limpiando los elementos del set (no confundir con del)
print(f"Set después de clear(): {my_other_set}")

# -- Juntando sets
programming_languages = {"Java", "Python", "JavaScript"}
brand_new_set = my_other_set.union(programming_languages)

print(f"Set fusionado: {brand_new_set}")
print(f"Buscando elementos diferentes en 2 sets: {brand_new_set.difference(my_other_set)}")