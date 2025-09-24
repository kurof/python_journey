"""__summary__

Día 9 del reto de Python: Condicionales!
Por default, las líneas en Python se ejecutan de forma secuencial
de arriba a abajo (siguiendo el orden en el que se escribieron),
si es necesario alterar el flujo, podemos hacerlo de 2 maneras:

    1. Ejecución condicional -> un bloque con una o más
       instrucciones se ejecutan si se cumple una condición.
    2. Ejecución repetitiva -> un bloque de una o más 
       instrucciones se repetirá si una condición se mantiene
       verdadera (True).

En este día veremos los condicionales: if, else, elif (también nos
serán útiles los operadores lógicos que vimos previamente!)

Reto original: Asabeneh
Tutoriales: MoureDev
"""

##### EJERCICIOS DE NIVEL 1
# --> Pide al usuario su edad y de acuerdo a su edad, brinda un mensaje
print("------- NIVEL 1 -------")
age = int(input("Introduce tu edad: "))

if age >= 18:
    print(f"La edad {age} es una edad adulta!")
else:
    print(f"Aún faltan {18 - age} años para los 18!")

# --> Comparando valores de input y otro
other_age = 28
if age > other_age:
    print(f"Eres {age - other_age} años mayor que la persona misteriosa!")
elif age < other_age:
    print(f"Eres {other_age - age} años más joven que la persona misteriosa!")
else:
    print("Tu edad y la de la persona misteriosa coinciden!")

# --> Pidiendo valores para comparar
a = int(input("\nIntroduce un número entero: "))
b = int(input("Introduce otro número entero: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print("Los números son iguales!")

##### EJERCICIOS NIVEL 2
print("------- NIVEL 2 -------")

score = int(input("Calificación 0-100 (sin decimales): "))
if score <= 100 and score >= 90:
    print(f"{score} -> A")
elif score <= 89 and score >= 70:
    print(f"{score} -> B")
elif score <= 69 and score >= 60:
    print(f"{score} -> C")
elif score <= 59 and score >= 50:
    print(f"{score} -> D")
else:
    print(f"{score} -> F")

# --> Checando temporada (decidí hacer varias listas para comparar)
spring = ["Marzo", "Abril", "Mayo"]
summer = ["Junio", "Julio", "Agosto"]
fall = ["Septiembre", "Octubre", "Noviembre"]
winter = ["Diciembre", "Enero", "Febrero"]

user_month = input("\nIntroduce un mes: ")
user_month = user_month.capitalize() # para hacer mayuscula la primera letra
# print(user_month)
if user_month in spring:
    print(f"{user_month} está en primavera")
elif user_month in summer:
    print(f"{user_month} está en verano")
elif user_month in fall:
    print(f"{user_month} está en otoño")
elif user_month in winter:
    print(f"{user_month} está en invierno")
else:
    print(f"{user_month} no es un mes válido!")

##### EJERCICIOS NIVEL 3
print("\n------- NIVEL 3 -------")

# --> Haciendo un diccionario con datos
person = {
    "name" : "Vitani",
    "last_name" : "Lavellan",
    "age" : 28,
    "country" : "Anderfels",
    "is_married" : True,
    "skills" : ["Magia", "Magia de Velo", "Alquimia", "Costura"],
    "game" : ["Dragon Age: Inquisition", "Dragon Age: The Veilguard"]
}

# --> Viendo si la key "skills" existe e imprimiendo los elementos del medio
if "skills" in person:
    print(person["skills"][1:3]) #asumiendo que sabemos la cantidad

# --> Viendo si la skill "Costura" existe e imprimimos
if "skills" in person and "Costura" in person["skills"]:
    print("Hay \"Costura\" entre las habilidades")

# --> Viendo si el personaje es casado y vive en los Anderfels
if person["is_married"] and person["country"] == "Anderfels":
    print(f"{person["name"]} está casado, vive en {person['country']}.")