"""_summary_
Una tupla es una colección de distintos tipos de datos, es
ordenada y NO se puede cambiar (inmutable). Estas se declaran
con paréntesis ().

    - Una vez que se crea una tupla, sus valores no pueden
      cambiarse
    - No podemos usar acciones como: add, insert, remove
    - Sus métodos son:
        - tuple() -> definición de tupla
        - count() -> conteo de un elemento en la tupla
        - index() -> encontrar el índice de un elemento
                     específico
        - Extra -> se puede concatenar una tupla con otra

Reto original: Asabeneh
Tutoriales: MoureDev
"""

#### ---- EJERCICIOS NIVEL 1
print("-----> Ejercicios nivel 1 <-----")
fem_names = ("Agatha", "Vitani", "Ashara")
male_names = ("Garreth", "Ofir", "Carver")

# -> Concatenando
names = fem_names + male_names
print(f"Lista combinada: {names}")

# -> Contando elementos
print(f"Total de personajes: {len(names)}")

# -> Cambiando y alterando la tupla
names = list(names)

names.append("Alistair")
names.append("Nathaniel")
names.append("Fenris")
names.append("Cullen")

# -> Regresando a tupla
names = tuple(names)
print(f"\nTupla con nuevos elementos: \n{names}")

print(f"Tamaño de tupla: {len(names)}")

# --> Quitando los últimos 4 elementos (los más nuevos)
print(f"Quitando los 4 últimos elementos:\n {names[0:6]}")

### ----> EJERCICIOS NIVEL 2
print("\n-----> Ejercicios nivel 2 <-----")

# --> Creando tuplas nuevas
fruits = ("Manzana", "Pera", "Fresa", "Guayaba")
vegetables = ("Calabacita", "Brocoli", "Zanahoria", "Chayote")
animal_products = ("Leche", "Mantequilla", "Queso", "Carne")

# --> Concatenando
food_stuff = fruits + vegetables + animal_products
print(f"Lista completa de comidas:\n {food_stuff}")

# --> Quitando el elemento del medio
print("Tamaño: ", len(food_stuff))

# 0 1 2 3 4 {5 6} 7 8 9 10 11 <- guia
food_stuff = list(food_stuff) # cambiando a lista
del food_stuff[5:7] # para que se tome el 6

print(f"Sin los elementos del medio: {food_stuff}")

# --> Quitando 3 elementos del inicio y 3 del final
del food_stuff[0:3]
print(f"\nSin 3 elementos del inicio: {food_stuff}")
print("Tamaño: ", len(food_stuff))

del food_stuff[4:7]
print(f"Adicional: sin los 3 elemtnos del final -> {food_stuff}")

# --> Regresando a tupla
food_stuff = tuple(food_stuff)

# --> Borrando completamente la tupla
del food_stuff