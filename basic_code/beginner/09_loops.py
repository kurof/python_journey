"""__summary__
Hemos llegado a los bucles/ciclos/loops, es un mecanismo
que nos sirve para iterar: repetir algo mientras cumpla
una condición.
En esta lección veremos los diferentes bucles que tenemos
en programación POO. 
    - While
    - Do while
    - For

--- Nota importante: Siempre hay que poner un incremento, 
    para que el ciclo pueda parar en algún punto!
"""

#### --- CICLO WHILE -> Mientras True, ejecuta una acción
print("------ > Usando WHILE < ------")
my_condition = 0

while my_condition <= 10:
    print(my_condition) # se imprimirá 1-10 gracias a lo de abajo
    my_condition +=2 # incrementando para que pueda detenerse!
else:
    # Wow! podemos usar else en caso de que ya no se cumpla la condición!!
    print("La condición ya no se cumple")


# usando otro loop
print("\nOtra condición:")
# no estaba funcionando el bucle inicialmente porque tenía 100 en lugar de 10

while my_condition < 20:
    if my_condition == 15:
        print("La condición es 15!")
        break # para detener la ejecución 

    my_condition += 1
    print(f"La condición es menor a 20: {my_condition}")

print("La ejecución continua")


#### ---> FOR -> Para iterar un listado de elementos (recorrer pue)
#                Se ejecuta un código varias veces acorde a los elementos
#                a iterar. Cualquier estructura de datos es iterable.
# vamos a hacer una lista
print("\n------ > Usando FOR < ------")
my_list = [35, 24, 28, 62, 52, 30, 30, 17]
my_tuple = {"Fanny", "GM", 28, "Python"} 
my_dict = {"Nombre":"Fanny", "Apellido": "GM", "Edad": 28, "Lenguaje": "Python"}

print("\nPara lista:")
for element in my_list: 
# creo que en este caso no es necesario un incremento
    print(f"Elemento lista: {element}")


print("\nPara tupla")
for element in my_tuple:
    print(f"Elemento tupla: {element}")

print("\nPara diccionario:")
# for element in my_dict.values(): <-- otra forma, para imprimir values
for element in my_dict:
    print(f"Elemento dict: {element, my_dict.get(element)}")

    # usando if
    if element == "Edad":
        print("checkpoint")
        break # rompemos el ciclo en cuanto llegue a edad
        # continue # esto haría que el ciclo se reinicie y pase a otra iteracion
else:
    print("Ya no hay más elementos en diccionario :0")