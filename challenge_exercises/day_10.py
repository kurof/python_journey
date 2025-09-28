"""_summary_
Whooo!!! Primera meta de 10 días del reto de Python!
Felicidades, Fanny (yo misma lol), has hecho un gran esfuerzo!

--

Día 10 del reto Python, hoy veremos: loops/ciclos/bucles
Estos los usamos para tareas que son repetitivas, Python (y 
otros lenguajes) nos proporcionan 2 tipos de bucles:

    1. While -> usado para ejecutar un bloque de código de
       forma repetida hasta que se cumpla una condición; una
       vez que se cumpla esta condición, se ejecutan las líneas
       siguientes al bucle.
    2. For -> Python tiene una ligera diferencia con otros 
       lenguajes a la hora de escribirse, pero su propósito
       es para iterar sobre una secuencia, una estructura de
       datos (listas, tuplas, diccionarios, sets o strings)

Como dato curioso: en Python es posible agregar un elemento
"else" a nuestro código, para cuándo queramos ejecutar otro
bloque de código después de que se cumpla la condición.
"""

##### EJERCICIOS NIVEL 1
# --> Iterando de 0 a 10
print("-- Iterando con for (0-10) --")
for i in range(11):
    print(i)

print("-- Iterando con while (0-10) --")
i = 0
while i <= 10:
    print(i)
    i += 1

# --> Iterando de 10 a 0
print("-- Iterando con for (10-0) --")
for i in range(10,-1,-1): # poniendo -1 para que cuente el 0
    print(i)

print("-- Iterando con while (10-0) --")
i=10
while i >= 0:
    print(i)
    i -= 1

# --> Imprimiendo un triangulo
print("\n-- Imprimiendo triangulo --")
for c in range(7):
    # usando if
    if c == 0:
        print("#")
    elif c == 1:
        print("##")
    elif c == 2:
        print("###")
    elif c == 3:
        print("####")
    elif c == 4:
        print("#####")
    elif c == 5:
        print("######")
    elif c == 6:
        print("#######")

# --> Usando loops anidados 
print("\n--- Usando nidados ---")
for i in range(2): # 2 vueltas al ciclo de abajo 
    for a in range(4): # 4 ejecuciones de este ciclo
        print("# # # # # # # #")

# --> Imprimiendo una multiplicacion por el mismo numero
print("\n----> Multiplicando el mismo numero de iteracion <----")
for i in range(11): # para que se tome el 10
    print(f"{i} x {i} = {i*i}")

# --> Me saltaré aquí algunos ejercicios de listas
# --> Iterando de 0 a 100 pero solo imprimo los numeros pares
print("\n---- Iterando de 0-100 y solo pares ----")
i=0
while i <= 100:
    i += 1
    if i%2 == 0:
        print(i)


######## EJERCICIOS NIVEL 2
# --> Iterando 0-100 e imprimiendo la suma de todo
print("\n---- Sumatoria de todos los numeros ----")
i=0
total = 0
while i <= 100:
    i += 1
    total += i
print(f"Suma total: {total}")

# --> Iterando 0-100 pero sumando por separado pares y nones
print("\n---- Sumatoria de pares y nones ----")
total_par, total_none = 0, 0
for i in range(101): # para que se tome el 100
    if i%2 == 0:
        total_par += i
    else:
        total_none += i
print(f"Total pares: {total_par} \nTotal nones: {total_none}")

###### EJERCICIOS NIVEL 3
countries = ["England", "Germany", "Mexico", "Argentina", "Switzerland"]

print("\n---- Imprimiendo paises con \"land\" ----")
for country in countries:
    if country.endswith("land"): # si tiene terminacion land = imprime
        print(country)

# --> Revirtiendo lista con loop
print("\n---- Revirtiendo lista con loop ----")
fruits = ["Banana", "Orange", "Mango", "Lemon"]

for i in range(len(fruits), 0,-1):
    print(fruits[i-1]) # imprime el index anterior, para que siga dentro del rango