"""_summary_

Día 11 del reto Python, la lección de hoy es: Funciones.
Una función es un bloque de código reutilizable diseñado
para cumplir cierta tarea. Para definir o declarar una
función, hacemos uso de la palabra reservada: def, 
seguido del nombre de la función, agregamos parámetros
(si son necesarios) y abajo agregamos las líneas de código.

Una función solo se ejecutará si la llamamos!

Reto original: Asabeneh
Tutoriales: MoureDev

El siguiente código contiene los ejercicios de este día
del reto!
"""

### --> Declarando una función
import math
from sre_compile import isstring

print("========= EJERCICIOS NIVEL 1 ==========")
def add_two_numbers(number_a : int, number_b : int):
    return number_a + number_b

print(f"Suma de dos numeros: {add_two_numbers(10,5)}")

# --> Función para declarar area de un circulo
def area_of_circle(r):
    area = round(math.pi * pow(r,2),2)
    return area

print(f"Área de un círculo: {area_of_circle(2)}")

# --> Función para recibir varios argumentos y sumarlos
# También verificar si son números y avisar si no lo son
def add_all_nums(*nums):
    total = 0 # para almacenar la suma

    for num in nums: # recorriendo los argumentos entrantes
        if isstring(num): # si hay un elemento string 
            print("Hay un string entre los argumentos!")
        else: # de lo contrario, sumamos los demás numeros
            total += num

    return total # devolvemos la suma final

sum_arguments = add_all_nums(10,5,5,0.5,"Hola")
print(f"Usando varios argumentos: {sum_arguments}")

# --> Función para convertir celsius a farenheit
print("\n--- Función para convertir C° a F° ---")

def convert_celsius_to_farenheit(c):
    f = (c * (9/5)) + 32
    return f

print(f"C° a F° -> {convert_celsius_to_farenheit(15)}°")

# --> Calculando la pendiente de una ecuación
# y = mx + b || -mx - b = - y || -mx = -y + b || m = (y+b) / x
print("\n--- Calculando pendiente ---")

def calculate_slope(x, y, b):
    m = (y+b)/x
    return m

print(f"Pendiente de 2x + 3y = 32 -> {calculate_slope(2,3,32)}")

# --> Solucionando ecuaciones cuadráticas (ax² + bx + c)
def solve_quadratic_eqn (x):
    a, b = 2, 6
    c = 10
    solution = (a*pow(x,2)) + (b * x) + c
    return solution

print(f"Solución ecuación cuadrática: {solve_quadratic_eqn(2)}")

# --> Declarando función que reciba una lista
print("\n--- Función que recibe una lista ---")
def print_list(a_list : list):
    for element in a_list:
        print(element)

chars = ["Vitani", "Garreth", "Agatha"]
print_list(chars)

# --> Función que revierte una lista
print("\n--- Revirtiendo lista ---")
def revert_list(a_list : list):
    for element in range(len(a_list),0,-1):
        print(a_list[element-1])

revert_list(chars) # invocando función

# --> Función para agregar elementos a una lista
print("\n--- Agregando elementos a lista ---")
def add_item(a_list : list, new_element):
    a_list.append(new_element) # agregando elemento

add_item(chars, ["Ashara", "Ofir"]) # se pueden agregar listas
print_list(chars)

####### EJERCICIOS NIVEL 2
print("========= EJERCICIOS NIVEL 2 ==========")

# --> Función que cuenta el total de pares y nones en un rango
def evens_and_odds(n : int):
    # variables para contar
    evens_count = 0
    odd_count = 0 

    # loop
    for i in range(n + 1): # para que se tome en cuenta todo
        # condiciones
        if i % 2 == 0:
            evens_count += 1
        else:
            odd_count += 1
    
    return evens_count, odd_count # regresamos los valores

print(f"Conteo de pares y nones en un rango de 100: {evens_and_odds(100)}")

# --> Función para factorial
print("\n--- Factorial de un número ---")
def factorial(n : int):
    n_factorial = 1 # para almacenar el factorial
    if n <= 0: # no hay factoriales con 0 o negativos
        return "Por favor, escribe un número positivo entero :D"
    else:
        for i in range(1, n+1):
            n_factorial *= i # haciendo el calculo n! = n * (n-1) * ...
        return n_factorial
    
print(f"Calculando factorial: {factorial(5)}")

## --> Calculando promedio de una lista
print("\n--- Calculando promedio de una lista ---")
def calculate_mean(a_list : list):
    total = 0
    # loop para recorrer la lista
    for element in a_list:
        total += element # sumando
    
    mean = total / len(a_list) # promedio
    return mean

numbers = [10,15,2,5,7]
print(f"Promedio de una lista: {calculate_mean(numbers)}")

####### EJERCICIOS NIVEL 3
print("========= EJERCICIOS NIVEL 3 ==========")

# --> Función para ver si un número es primo
print("\n--- Verificando si un número es primo ---")
def is_prime(n: int):
    if n <= 1: # no hay primos con 0, 1 o negativos
        return False
    for i in range(2, int(math.sqrt(n)) + 1): # recorriendo hasta la raíz cuadrada
        if n % i == 0: # si es divisible por cualquier número
            return False # no es primo
    return True # si no es divisible por ningún número, es primo

print(f"¿El número 7 es primo? {is_prime(7)}")