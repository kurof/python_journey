"""_summary_
Aquí pondré algunos ejemplos extras de operadores de 
comparación en Python. Así como los ejercicios del 
día 3 del challenge de Python.

Reto original: Asabeneh
Tutoriales: MoureDev
"""

# ---> Comparadores extra en Python (aunque es mejor usar los comparadores comunes)
# print(f"1 is 1 -> {1 is 1}") # devuelve True si los elementos coinciden
# print(f"1 is not 2 -> {1 is not 2}") # devuelve True si No son el mismo objeto
import math


print(f"Fa in Fanny -> {"Fa" in "Fanny"}") # devuelve si un elemento está en un list
print(f"B not in Fanny -> {"B" not in "Fanny"}") # devuelve True si el elemento no está

# --> Ejercicios de operadores
print("---> Haciendo cálculos en un triángulo <---")
base = float(input("Ingresa base: "))
height = float(input("Ingresa altura: "))
side = float(input("Ingresa medida del otro lado del triángulo: "))

triangle_area = (base * height)/2
perimeter = base + height + side
print(f"Área del triángulo: {triangle_area}")
print(f"Perimetro del triángulo: {perimeter}")

print("\n--> Haciendo cálculos en un rectángulo <---")
rectangle_length = float(input("Ingresa la base del rectángulo: "))
rectangle_heigth = float(input("Ingresa la altura del rectángulo: "))

rectangle_area = rectangle_length * rectangle_heigth
rectangle_perimeter = 2* (rectangle_heigth + rectangle_length)

print(f"Área del rectángulo: {rectangle_area}")
print(f"Perímetro rectángulo: {rectangle_perimeter}")

print("\n---> Haciendo cálculos en un círculo <---")
circle_radius = float(input("Ingresa el radio del circulo: "))

circle_area = math.pi * (circle_radius**2)
print(f"Área del círculo: {circle_area}")

# ---> Lo dejaré así, siento que muchos ejercicios son redudantes para lo que tengo