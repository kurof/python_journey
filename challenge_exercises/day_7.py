"""_summary_
Día 7 del reto de Python: SETS

Un set es una colección de elementos; es una colección de
elementos SIN orden y SIN índice, es usada para almacenar
items únicos y podemos usar cosas como union, intersection,
difference, symmetric difference, subset, super set y 
disjoint set, entre otros conjuntos.

El siguiente archivo contiene ejercicios del reto que van 
desde el nivel 1 al 3
"""

# --> Creando sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

##### EJERCICIOS NIVEL 1
print("--------- Ejercicios nivel 1 ----------")
print(f"Tamaño del set de compañías: {len(it_companies)}")

# --> Agregando Twitter/X al set
it_companies.add("Twitter/X")

# --> Agregando multiples compañías
videogame_companies = {"Blizzard", "EA", "Bioware", "Riot"}
it_companies.update(videogame_companies)

print(f"Set actualizado: \n{it_companies}")

# --> Quitando un elemento del set
it_companies.remove("Facebook")
print(f"Sin Facebook: {it_companies}")

# -> ¿Cuál es la diferencia entre remove() y discard()?
# Si bien ambas quitan elementos de un set, discard() NO
# dará error si el elemento a descartar no existe,
# mientras que remove() sí dará error si el elemento no
# está en el set.

### EJERCICIOS NIVEL 2
# --> Juntando los sets A y B
print("\n--------- Ejercicios nivel 2 ----------")
C_join = A.union(B)
print(f"Set fusionado entre A y B: {C_join}")

# --> Encontrando la intersección entre A y B
print(f"Intersección entre A y B -> {A.intersection(B)}")

# --> ¿A es un subset de B?
print(f"¿A es subset de B? {A.issubset(B)}")

# --> ¿A y B son sets disjoint? (o sea, si no tienen coincidencias entre si)
print(f"¿A y B son disjoint sets? {A.isdisjoint(B)}")

# --> Diferencia simetrica entre A y B, elementos que no comparten ambos
print(f"Diferencia simétrica: {A.symmetric_difference(B)}")

# --> Borrando completamente ambos sets
del A, B

#### EJERCICIOS DE NIVEL 3
# --> Convirtiendo la lista en un set
age_set = set(age)

# tamaños de los conjuntos de datos
list_size = len(age)
set_size = len(age_set)

print(f"Es {list_size} más grande que {set_size} -> {list_size > set_size}")

## Explica la diferencia entre: string, list, tuple y set
#   - Un string es una cadena de texto, es todo aquello que 
#     tenga que ver con el uso de texto en el programa (como
#     imprimir un mensaje o algo así)
#   - Una lista es un tipo de estructura de datos ORDENADA,
#     podemos poner todo tipo de datos y acceder a ellos, así
#     como agregar, eliminar, contar, etc.
#   - Una tupla es otra estructura ordenada, pero aquí NO 
#     se pueden manipular los datos, no podemos cambiar el 
#     contenido.
#   - Un set es un conjunto de datos NO ORDENADOS, es decir,
#     no tiene un orden específico por lo que no es posible 
#     acceder de forma convencional como en las estructuras
#     y tampoco permite duplicados!

phrase = "I am a teacher and I love to inspire and teach people"

# --> Separando la frase en varios pedazos
phrase_set = set(phrase.split(" "))
print(f"\nFrase original: {phrase}")
print(f"Set de la frase (sin repeticiones): \n{phrase_set}")
print(f"Palabras totales, sin contar repetidos: {len(phrase_set)}")