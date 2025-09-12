"""_summary_
Día 2 del challenge 30 días de Python: variables y funciones del 
sistema. Se tendrán que crear algunas variables y se trabajaran 
funciones predeterminadas de Python con ellas.

En esta ocasión, pondré todo los niveles de los ejercicios.

Reto original por: Asabeneh
Complementado con el curso de: MoureDev
"""

# Creando variables (ejercicio nivel 1)
import math


first_name = input("Escribe tu primer nombre: ")
last_name = input("Escribe tus apellidos: ")
full_name = first_name + " " + last_name
country = "México"
city = "Querétaro"
age = 28
current_year = 2025
is_married = False
is_true, is_light_on = True, False

# Viendo el tipo de variable (nivel 2 del ejercicio), no lo haré con todo
print(type(full_name))

print(f"Tamaño de los nombres: {len(first_name)}") #viendo el tamaño con len()
print(f"Mismo tamaño de nombre y apellidos: {len(first_name) == len(last_name)}")

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_two ** num_one
floor_division = num_one // num_two

print(f"Uso de: {num_one} y {num_two}\nSuma: {total} \nResta: {diff}")
print(f"Multiplicación: {product} \nDivisión: {division}")
print(f"Módulo: {remainder} \nPotencia: {exp} \nFloor division: {floor_division}")

# Cálculo del área de un circulo de 30m de radio
radius = int(input("Favor de introducir el radio del circulo: "))
area_of_circle = round(math.pi * (radius**2), 1) #pi * r²
circum_of_circle = round((2 * math.pi * radius), 1)

print(f"Área del circulo: {area_of_circle} \nCircunferencia: {circum_of_circle}")