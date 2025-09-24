"""__summary__
Esta lección será sobre Diccionarios en Python, los
cuales funcionan de forma similar a los hashmaps en
otros lenguajes. Guarda elementos con una clave y un
valor.
Que es lo que tienen los diccionarios:

    - Se pueden declarar con la palabra: dict()
    - Se puede recurrir a las llaves para declarar {}
        - Si bien es confuso hacer uso de llaves porque
          así se pueden declarar los sets... la verdad
          es que estamos declarando siempre un diccionario
          hasta que se agreguen elementos.
        - El contenido del diccionario también tiene un
          FORMATO DIFERENTE, algo como: {"Key" : "Valor", "Key": "Valor"}
          como en los hashmaps en java!
            - Aunque no es necesario tener que se muy explicitos en el tipo
            de dato

Es muy sencillo acceder a sus elementos a través de la clave (key) que exista
dentro del diccionario.
"""

my_dict = dict() # una forma de declarar
my_other_dict = {} # otra forma de declarar

# --> Agregando elementos
my_other_dict = {"Nombre" : "Fanny", "Apellido" : "GM", "Edad" : 28, 1 : "Python"}
my_dict = {
    "Nombre" : "Agatha",
    "Apellido" : "Surana",
    "Edad" : 25,
    "Facción" : {"Guardas Grises", "Círculo de magos"},
    1 : "Dragon Age: Origins"
}

print(my_other_dict)
print(my_dict)

# --> El tamaño de un diccionario se basa en la cantidad de claves existentes
print(f"Tamaño del diccionario (CUANTAS CLAVES TIENE): {len(my_dict)}")

# --> Accesando a elementos
print(f"Tomando un elemento: {my_dict["Nombre"]}")
print(f"Buscando elemento con key 1: {my_dict[1]}")

# --> Agregando elementos a un campo nuevo!
my_dict["Romance"] = "Alistair Theirin"

print(my_dict)

# --> Eliminando elementos específicos
del my_dict["Romance"]
print(my_dict)

# --> Comprobando si hay elementos en un diccionario
print(f"Está \"Agatha\" en my_dict: {"Agatha" in my_dict}") # saldrá que no porque no es key
print(f"Está \"Nombre\" en my_dict: {"Nombre" in my_dict}")

# --> Imprimiendo elementos (formato de lista)
print(f"Diccionario: \n{my_dict.items()}")
print(f"Keys del diccionario {my_dict.keys()}")
print(f"Valores del diccionario:{my_dict.values()}")

# --> Creando un diccionario nuevo SIN valores (se pueden agregar aqui)
#     pero a partir de claves (keys)
my_new_dict = dict.fromkeys(("Nombre", "Apellido", 1))
print(f"\nDiccionario nuevo: {my_new_dict}")

my_new_dict = dict.fromkeys(my_dict, "kurof") # tomando las claves de otro y agregando un valor
print(f"Diccionario clonado y valor para todo: {my_new_dict}")

# --> Transformando a otros tipos de estructuras
print("\n---- Conviritiendo a : ----")
print(f"--> Lista (solo keys) {list(my_new_dict)}")
print(f"--> Lista de values: {list(my_new_dict.values())}")

print(f"\n--> Tupla (keys por default): {tuple(my_new_dict)}")
print(f"--> Set (keys por default): {set(my_new_dict)}")