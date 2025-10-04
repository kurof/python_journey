"""_summary_

En esta versión veremos las funciones: al igual que en 
muchos otros lenguajes con POO, como Java, las funciones
se usan para resolver problemas con ellas.

Esto a través de encapsular lógica, instrucciones que puedan
ser usadas para resolver un problema específico y podamos
centralizar nuestro código para evitar repetir el mismo
código una y otra vez.

En Python, para definir una función hacemos uso de la palabra
reservada: def, seguido del nombre de la funcion, ponemos un
par de paréntesis () y dos puntos.
Las funciones son capaces de generar y recibir código 
"""

### --> Definiendo una función
def my_function():
    print("Esto es una función :D")

# --> Llamando a la función
my_function()

### --> Otra función, pero con parámetros!
# Ya que Python NO es un lenguaje tipado, como Java, pero
# podemos hacer un : int para indicar al desarrollador
# el tipo de dato que se espera para la función.
def sum_two_values(firts_value : int, second_value : int):
    total = firts_value + second_value
    print(f"Suma: {total}")

# llamando a nuestra otra funcion
sum_two_values(10,5)

### ---> Haciendo funciones que devuelvan datos!
def sum_values_with_return(first_value, second_value):
    return first_value + second_value # devuelve el valor de suma

my_result = sum_values_with_return(6,6) # podemos asignar esto a una variable
print(f"Función con return: {my_result}") # e imprimirla

### --> Otra función
def print_name(first_name :str, last_name : str):
    print(f"Tu nombre es {first_name} {last_name}")

# podemos agregar el nombre de los parámetros!
# así es posible mantener el orden de los elementos
print_name(last_name="GM", first_name="Fanny")

#### --> Funciones con valores predeterminados
def print_name_with_default (first_name, last_name, alias = "NA"):
    print(f"Tu nombre es: {first_name} {last_name} y tu alias: {alias}")

print_name_with_default("Fanny", "GM") # llamando sin poner el parámetro con default
print_name_with_default("Fanny", "GM", "kurof") # no hay problema si ponemos un alias

### --> Haciendo una función que reciba parámetros dinámicos
# Funciona mejor si usamos varias cosas del mismo tipo de dato
# Esto es conocido como parámetros arbitrarios, recibe varios pero es como
# si estuvieran separados.
def print_texts(*texts):
    # iterando textos
    for text in texts:
        print(text)

print_texts("hola")
print_texts("qué tal?")