"""_summary_
Hemos llegado finalmente a las condicionales!
Es la forma de representar los flujos en nuestro código,
ver qué acciones se hacen o no dependiendo de alguna 
acción.

La sintaxis es:
    - Se pone una condición a cumplir, y de ahí se pondrán
      las cosas que deberán realizarse en caso de que se 
      cumpla o no.
    - Se usa la palabra reservada "if"
    - Trabajamos con booleanos para hacer funcionar un if

Nota: al momento de poner una condición para un if, estamos
      asumiendo que esta deberá cumplirse, o sea, debe ser
      True!

Tutorial: MoureDev
"""

# ---> SINTAXIS DE UN CONDICIONAL IF
my_condition = False

if my_condition: # es lo mismo a poner my_condition == True
    print("La condición es True")

# Si la condición no se cumple, pasará directo a esta línea
# pero, aún así, aunque se cumpla la veremos vv
print("La ejecución continúa")

# usando otra condición
operacion = 1
if operacion == 10:
    print(f"La operación: 5*2 = {operacion} es igual a 10")

if operacion > 10 and operacion < 20: # poniendo 2 condiciones
    print("Es mayor que 10 y menor a 20")
elif operacion == 1:
    print("La operación es igual a 1")
else:
    print("El resultado es menor o igual a 10")

# usando strings en condicionales
my_string = ""

if not my_string: # negando que la cadena tiene texto
    print("La cadena no tiene texto")
    
if my_string == "Mi cadena de textooo":
    print("La cadena tiene un texto diferente a la condición")