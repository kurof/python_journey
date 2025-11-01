"""_summary_

Las expresiones regulares son un mecanismo/estándar que tenemos en muchos
lenguajes de programación, nos ayudan a ver si una cadena de texto contiene
ciertos elementos.
Es capaz de devolver no solo si contiene cierto elemento, si no que además,
es capaz de regresar las ocurrencias dentro de la cadena de texto.

Primero que nada, hay que importar el modulo re para poder trabajar con ello.

Una de las formas más comunes para usar RE es con expresiones personalizadas.
Podemos usar rangos de letras, números, también podemos hacer ciertos escapes
para evitar algunos caracteres especiales. Es un tema bastante amplio, no 
no estaría mal echarle un vistazo más adelante y aparte!
"""

### --> Importando
import re

my_string = "Esta es la lección número 20: Lección de Expresiones regulares"
my_other_string = "Esta NO es la lección número 19: Manejo de ficheros"

## --> Operación match, busca patrones dentro de un string
#      busca desde el inicio del string, pero puede toparse con ciertas cosas,
#      por lo que es conveniente poner una flag que indique a la función que
#      y no puede hacer
string_match = re.match("Esta es la lección", my_string, re.I) 
# ^ ver si hay este elemento en una cadena
print(string_match)

## --> Usando span, se ejecuta pero pone un error, pero es un atributo de match
#      el que nos indica el rango en el que se encuentra la coincidencia de la
#      búsqueda. Se compone de 2 elementos:
#           - El inicio de la coincidencia
#           - El final de la coincidencia
#      Es decir, las posiciones de cada elemento dentro del string que concuerde
span_start, span_end = string_match.span()

print(f"\nImprimiendo solo el fin e inicio de span: \n{my_string[span_start:span_end]}\n")

# Evaluando con un none
string_not_match= re.match("Esta NO es la lección", my_other_string, re.I)
# if not(string_not_match == None): # si el resultado NO es none
# if string_not_match is not None:
if string_not_match != None:
    span_start, span_end = string_not_match.span()
    print(my_other_string[span_start:span_end]) # recordar poner el STRING original

print(re.match("Expresiones regulares", my_string))

## --> Operación search, similar a match, busca una coincidencia dentro de un cadena
#      de texto; PERO aquí no necesariamente nos pone elementos desde el principio,
#      y nos devuelve la posición de la coincidencia
string_search = re.search("lección", my_string, re.I)
print(string_search)

start_span, end_span = string_search.span()
print(my_string[start_span:end_span])

## --> Operación findall, esta operación nos devuelve un listado de las coincidencias
#      de la palabra que estamos buscando dentro de un string. Podemos hacer que no
#      importe si esté en mayúsculas o minúsculas con re.I (ignore case).
string_findall = re.findall("lección", my_string, re.I)
print(string_findall)

## --> Operación split, separa una cadena de texto con un elemento que agregamos como
#      argumento, el elemento separará el string en partes que coincidan y las 
#      deposita en una lista. Busca patrones.
split_string = re.split(" ", my_other_string)
print(split_string)

## --> Operación sub, usado para sustituir elementos dentro de una cadena de texto.
#      Agregamos primero el elemento que deseamos sustituir, luego el elemento con
#      el que se va a sustituir y después la cadena de texto a la que pertenecerá!
#      Podemos agregar más de una opción con el pipe (|), por ejemplo:
#           - "[l|L]ección", "LECCIÓN", <string> (para cambiar sin importar l o L)
#           - "[lección|Lección]", "LECCIÓN", <string> (lo mismo pero más largo (?))
print(f"\nCambiando con sub: {re.sub("NO", "no", my_other_string)}") # cambiando NO por no

## --> Patterns, patrones personalizados y usando RE.
#      ¿Cómo podemos hacer un patrón que haga referencia a una expresión regular?
#      Podemos marcar un patrón a través del uso de una r, seguido de comillas
#      dobles o sencillas.
#           r"<expresión_regular>"
pattern = r"[lL]ección" # buscando lección con l o L!
print(re.findall(pattern, my_string)) # buscando el patrón que hicimos

pattern = r"[lL]ección|Expresiones" # el pipe podemos usarlo para más patrones!
print(re.findall(pattern, my_string))

pattern = r"[0-9]" # podemos buscar números!
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d" # buscando números en la cadena de texto
print(re.findall(pattern, my_string))

pattern = r"\D" # buscando las letras
print(re.findall(pattern, my_string))

pattern = r"[l]." # buscando variaciones con l en el string
print(re.findall(pattern, my_string))

## -> Nota: con el match es un poco difícil buscar patrones, pero es posible con
#           search.

### Patrón más complejo para expresiones regulares: una validación de email!
#   El siguiente patrón contiene:
#       - ^ para indicar que la cadena EMPIEZA CON, en este caso letras de la
#         "a" a la "z" tanto en mayúsculas como números, puntos, guiones bajos,
#         signo más (+) y guión corto (-)
#       - seguido de un arroba (@), solo 1
#       - Se buscan los mismos elementos después
#       - Se hace un escape de caracter (\), buscamos la terminación pero no un salto
#         de línea (se valida con cualquier elemento)
#       - $ soporte de strings,es decir, tendrá en cuenta todo lo que venga después de
#         ese punto, por ejemplo valdría algo como .com.mx, eso se debe especificar en 
#         el [], sin este escape nos tomaría la primera letra solamente 
email = "fgrom_15@python.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

print(f"\nFindall: {re.findall(pattern, email)}")
print(f"Match: {re.match(pattern, email)}")
print(f"Search: {re.search(pattern, email)}")

# probando con otro email sin todos los elementos
email = "frog_07@python.com"
print(re.findall(pattern, email))