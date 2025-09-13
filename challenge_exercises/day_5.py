"""__summary__
En este archivo se encuentran los ejercicios del día 5
del desafío de 30 días de Python, el tema son: LISTAS.

Los ejercicios van de nivel 1 a nivel 2.

Reto original: Asabeneh
Tutoriales: MoureDev
"""

# ----> Nivel 1
from statistics import mean, median


print("------- NIVEL 1 -------")
level_1_list = [] # declarando lista vacía
level_1_list = ["Dorian", "Alistair", "Cullen", "Zevran", "Blackwall"]

print("Lista original -> ", level_1_list)
print(f"Tamaño de la lista: {len(level_1_list)}")

# obteniendo elementos de la lista
print(f"\nPrimer elemento: {level_1_list[0]}")
print(f"Elemento del medio: {level_1_list[2]}")
print(f"Último elemento: {level_1_list[4]}")

mixed_data_types = ["Fanny", 28, 1.63, "Soltera", "Zibatá"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(f"\nDatos: {mixed_data_types}")
print(f"Tamaño de la lista de compañías: {len(it_companies)}")

# cambiando un elemento
it_companies[5] = "oracle"
it_companies.append("Indra")

print(it_companies[4].lower())
print(f"Existe \"Google\" en la lista: {"Google" in it_companies}")

it_companies.sort() # acomodando lista
print(f"Lista ordenada: {it_companies}")

# it_companies.reverse() # poniendo la lista al reves
# print(f"Lista al revés: {it_companies}")

# se tiene que agregar un lugar extra porque no se toma en cuenta el limite
three_first = it_companies[0:3]
print(f"Mostrando solo los 3 primeros elementos: \n{three_first}")

three_lasts = it_companies[-4:-1]
print(f"Mostrando los 3 últimos: {three_lasts}")

# removiendo elementos
it_companies.remove(it_companies[3])
print("Lista sin los elementos medio: ", it_companies)

print(f"\nQuitando el primer elemento: {it_companies.pop(0)} \nLista: {it_companies}")
print(f"Eliminando elementos del medio: {it_companies.pop(2), 
                                        it_companies.pop(3)} \nLista: {it_companies}")

# Eliminando elementos de la lista
it_companies.clear()
print("\nLista de compañías: ", it_companies)

# Borrando la lista entera
del it_companies # ya no se puede acceder

####### EJERCICIOS DE NIVEL 2
print("-------- NIVEL 2 --------")
ages = [19, 22, 19, 24, 25, 26, 24, 25, 24, 28]

print(f"\nTamaño de la lista: {len(ages)}")

ages.sort() # acomodando la lista
print(f"Lista original: {ages}")
print(f"Elemento máximo: {max(ages)} \nElemento mínimo: {min(ages)}")

# Agregando los elementos max y min
ages.append(28)
ages.append(19)

print(f"Lista añadida: {ages}")

# Encontrando la media de la lista de edades
ages_mean = round(mean(ages), 2)

print(f"\nMedia de la lista: {median(ages)}")
print(f"Promedio de la lista: {ages_mean}")

value_min = min(ages)
value_max = max(ages)

print(f"Rango de edades (max - min): {value_max - value_min}")

value_min_av = abs(value_min - ages_mean)
value_max_av = abs(value_max - ages_mean)

print(f"\nValor max -> {round(value_max_av, 2)}")
print(f"Valor mínimo -> {round(value_min_av, 2)}")