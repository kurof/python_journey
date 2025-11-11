"""_summary_

Día 18 del reto Python de 30 días! La lección de hoy es: Expresiones Regulares

Una expresión regular or RegEx es un string de texto especial que nos ayuda a 
encontrar patrones en los datos. Puede ser utilizada para verificar si un patrón
existe dentro de algún tipo de dato.
Este tipo de expresión no es solo exclusiva de Python, se encuentran en muchos
lenguajes de programación!

    - Es necesario importar el modulo re de Python para empezar a usar las 
      operaciones necesarias con RegEx (detectar o encontrar patrones)

Los métodos que podemos encontrar dentro de re (todas regresan las coincidencias
o nos retornan un None, en caso de no hacerlo):
    - re.match() -> busca un patrón o frase EN LAS PRIMERAS LINEAS DEL TEXTO
    - re.search() -> busca patrones o frases en todo el texto
    - re.findall() -> regresa una lista con todas las coincidencias que se
      puedan encontrar
    - re.split() -> toma un string y los divide de acuerdo a algún criterio, que
      se puede indicar dentro del método (por ejemplo, dividir un texto a partir
      de los puntos que pueda tener) y nos devuelve una lista con el texto nuevo
    - re.sub() -> reemplaza una o más coincidencias dentro de un string

También, si queremos trabajar con expresiones regulares creadas por nosotros, hay
que hacer uso del siguiente formato:

    r"{RegEx personalizado}"
    r'{RegEx personalizado}'

Reto original: Asabeneh
Tutoriales: MoureDev
"""

##### --> EJERCICIOS DE NIVEL 1
## --> ¿Qué palabra es la que se repite más?
import re


paragraph = "I love teaching. If you do not love teaching what " \
"else can you love. I love Python if you do not love something " \
"which can give you all the capabilities to develop an application " \
"what else can you love"

# Capturando elementos:
word_capture = [
    re.findall(r"\D[I]", paragraph),
    re.findall(r"love", paragraph),
    re.findall(r"teaching", paragraph),
    re.findall(r"If", paragraph),
    re.findall(r"you", paragraph),
    re.findall(r"do", paragraph),
    re.findall(r"not", paragraph),
    re.findall(r"what", paragraph),
    re.findall(r"else", paragraph),
    re.findall(r"can", paragraph),
    re.findall(r"Python", paragraph),
    re.findall(r"if", paragraph),
    re.findall("something", paragraph),
    re.findall("which", paragraph),
    re.findall("give", paragraph),
    re.findall("all", paragraph),
    re.findall("the", paragraph),
    re.findall("capabilities", paragraph),
    re.findall("to", paragraph),
    re.findall("develop", paragraph),
    re.findall(r"[^c]an", paragraph),
    re.findall("application", paragraph)
]

word_count = {}

# pasamos por cada lista de palabras ej: [i, i, i]
for list_word in word_capture:
      # Hacemos el conteo de los elementos y ponemos el primer elemento de
      # cada lista interior (ponemos el primer elemento como indicador)
      print(list_word.count(list_word[0]), " : ", list_word[0])

## --> La posición de algunas particulas en el eje horizontal son -12, -4, -3
#      y -1 en la dirección negativa, 0 como inicio, 4 y 8 en la dirección
#      positiva. Extrae estos números del texto entero y encuentra la distancia
#      entre los dos puntos más lejanos.
points = "-12, -4, -3, -1, 0, 4, 8"
p_match = r"-?\d+" # se toman los números que tengan o no un -

points_list = re.findall(p_match, points) # pasando el string a lista
sorted_list = [int(p) for p in points_list] # pasando elementos a int y pasando a lista
diff = max(sorted_list) - min(sorted_list) # diferencia entre punto máximo y minimo

print(f"Lista de números: {sorted_list}")
print(f"Diferencia entre punto máximo y mínimo: {diff}")

##### --> EJERCICIOS DE NIVEL 2
## --> Escribe un patrón que identifique si un string es una variable valida de python
def is_valid_variable(text : str):
      # se recurrió a copilot  para el patrón n.nU
      # pattern detects invalid Python identifiers:
      # - starts with a digit (?:^\d)
      # - contains any character other than letters, digits or underscore
      pattern = r'(?:^\d)|[^_a-zA-Z0-9]'
      pattern_find = re.findall(pattern, text)

      if pattern_find:
            return "Nombre de variable NO valido"
      else:
            return f"Variable: {text} es válida"
      
print(is_valid_variable("1first_name"))

##### --> EJERCICIOS DE NIVEL 3
## --> Limpia el siguiente texto; después de eso, cuenta las 3 palabras más 
#      frecuentes

# Funcion para limpiar el texto
def clean_text(text : str):
      # Pattern es:
      # - Tomar todos las letras de la a-z (mayus y minus)
      # - Signos de interrogación (?)
      # - Puntos, comas y espacios
      pattern = r"[a-zA-Z.,?\s]"
      clean_sentence = ""
      text_wo_noise = re.findall(pattern, text)

      # Dado que nos regresa una lista con las letras, las
      # acomodamos en un nuevo string (clean_sentence)
      for letter in text_wo_noise:
            clean_sentence += letter

      return clean_sentence


def most_frecuent_words(clean_result : str):
      """ Acepta una entrada de texto, hecha para el resultado
      en la función: clean_text. 
      Devuelve un conteo de palabras
      más frecuentes en el texto de argumento.
      """
      # Pasando las palabras a una lista
      word_list = [word.strip(".,?") for word in clean_result.lower().split() if word]


      word_count = {
            word : word_list.count(word)
            for word in set(word_list)
      }
      
      word_count_sorted = sorted(word_count.items(), 
                    # recorremos elementos del dict
                    # si un elemento tiene un valor mayor a 1
                    # se va hasta arriba
                    key= lambda w : w[1], reverse=True)
      
      return word_count_sorted[0:7] # regresando primeros valores

sentence = "%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. "\
           "There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. "\
           ";I found tea@ching m%o@re interesting tha@n any other %jo@bs. "\
           "%Do@es thi%s mo@tivate yo@u to be a tea@cher!?"

ct = clean_text(sentence)
print(ct)
print(most_frecuent_words(ct))