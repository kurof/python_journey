# ----> OPERADORES comunes (también aplica a otros lenguajes)

### OPERACIONES ARITMETICAS
#Uso de operandos simples
print("---- Operandos ----")
print(f"Suma -> {3} + {4} =  {3+4}")
print(f"Resta -> {3} - {4} = {3-4}")
print(f"Multiplicación -> {3} * {4} = {3*4}")
print(f"División -> {3} / {4} = {3/4}")

#Uso de operandos poco convencionales
print(f"Módulo -> {3} % {4} = {3%4}")
print(f"Exponencial -> {3} ** {4} = {3**4}")
print(f"Floor division -> {3} // {4} = {3//4}")

# El simbolo + tambien nos sirve para concatenar strings
print("Hola " + "Python")

# Si quisieramos concatenar con algun elemento que NO sea strings:
print("Hola " + str(15))

# Algo curioso (solo funciona con int):
print("ora " * 5)


## OPERACIONES COMPARATIVOS
# Solo se imprimirá True o False usamos 3 y 4
print(f"Mayor a (>): {3 > 4}")
print(f"Menor a (<): {3 < 4}")
print(f"Mayor o igual a (>=): {3 >= 4}")
print(f"Menor o igual a (<=): {3 <= 4}")
print(f"Igual a (==): {3 == 4}")
print(f"Diferente a (!=): {3 != 4}")

# Si comparamos strings, se iria por el orden alfabetico
# pero también es case sensitive

## OPERADORES LOGICOS (en Python lo escribimos como tal)
print(f"Usando AND : {3 > 4 and "Hola" > "Python"}") # Esto es el &&
print(f"Usando OR: {3 > 4 or "Hola" > "Python"}") # Esto es el ||
print(f"Usando NOT: {not(3 > 4)}") # Esto es el !<elemento>