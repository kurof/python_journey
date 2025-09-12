# Usando Strings
# Nota: es case sensitive

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

# -- Usando caracteres especiales
print("Este es un string con:\nSalto de línea :D")
print("\tEste es un string tabulado :0")

# -- Haciendo el escape de los elementos especiales (\\)
print("\\tEstamos ignorando la tabulación\\ny el salto de línea!")

# -- Formateando strings
name, last_name, age = "Fanny", "GM", 28
# si queremos imprimir como tal vv
print("Mi nombre es {} {} y mi edad es {}".format(name, last_name, age)) #recomendada por mouredev
# si queremos imprimir los elementos con un tipo especifico vv (seguro)
print("Mi nombre es %s %s y mi edad es %d" %(name, last_name, age))

print(f"Mi nombre es {name} {last_name} y mi edad es {age}") #otra opcion y mi fav

### --- Desempaquetando caracteres (solo como dato la verdad)
language = "python"
a,b,c,d,e,f = language # esto dividirá la palabra en caracteres

print(a)
print(b)
print(e)
print(f)

# -- División de un string
# language_slice = language[1:] # podemos poner las posiciones que queremos
# language_slice = language[1:3]
# language_slice = language[-2]
language_slice = language[0:6:2] #tomando elementos dentro del rango
print(language_slice)

# -- String revertido
reversed_language = language[::-1]
print(reversed_language)

# -- Funciones con strings
print(language.capitalize()) # pone en mayuscula la primera letra
print(language.upper()) # todo en mayusculas
print(language.count("t")) # cuenta un elemento especifico
print(language.isnumeric()) # nos indica si es numero o no
print("5".isnumeric())
print(language.lower()) # pone las letras en minusculas

print(language.upper().isupper()) # pasa a mayusculas y evalua si esta en mayus
print(language.startswith("py")) # ver si empieza con algo