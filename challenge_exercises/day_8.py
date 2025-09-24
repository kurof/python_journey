"""_resumen_

Día 8 del reto Python: Diccionarios (Dictionaries).
Un diccionario es una colección de datos de varios tipos, 
no es ordenada, se puede modificar y está emparejada, es
decir, se acomoda en un estilo: key (clave) : value (valor).

    - Para crear un diccionario hacemos uso de llaves {} 
        - Que si bien parece un set, al momento de poner los datos 
          como key : value, o con la palabra reservada dict()
    - Para acceder a elementos usamos el nombre de la key.
        - Podemos comprobar primero si existe esta clave con el 
          método get()
"""

#### EJERCICIOS
# --> Creando un diccionario
dog = {
    "Name" : "Ringo",
    "Color" : "Café grisaceo",
    "Breed" : "Pitbull",
    "Patas" : 4,
    "Edad" : 2
}

# --> Haciendo otro diccionario
student = {
    "first_name" : "Fanny",
    "last_name" : "GM",
    "genero" : "Femenino",
    "edad" : 28,
    "estatus marital" : "Soltera",
    "habilidades" : ["Python", "Java", "JavaScript", "C#"],
    "país" : "México",
    "ciudad" : "Querétaro",
    "dirección" : "Zibatá"
}

print(f"Lista del estudiante python: \n{student}")

# --> Mostrando el tamaño del diccionario
print(f"\nTamaño del diccionario: {len(student)}")

# --> Obteniendo el valor del elemento "habilidades"
print(f"¿Está la key: skills? {"skills" in student}")
print(f"¿Está la key: habilidades? {"habilidades" in student}")
print(f"Habilidades (lista): {student["habilidades"]}")
print(f"Tamaño de habilidades: {len(student['habilidades'])}")

# --> Agregando elementos al diccionario (habilidades)
student.update({"habilidades" : ["Python", "Java", "JavaScript", "HTML"]})
print(student["habilidades"])

# --> Mostrando las keys en formato de lista
print(f"\n\nKeys del diccionario: {list(student.keys())}")

# --> Mostrando los values en formato de lista
print(f"Values del diccionario: {list(student.values())}")

# --> Cambiando el diccionario a una lista de tuplas con items()
print(f"Mostrando el diccionario en tuplas: \n{tuple(student.items())}")

# --> Borrando un elemento del diccionario
student.popitem() # eliminando el último punto
print(student)

# --> Borrando un diccionario
del student
print(f"\nDiccionario existente: {dog}")