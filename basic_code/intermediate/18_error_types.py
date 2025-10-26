"""_summary_

Vamos a hacer un repaso sobre las excepciones que puede lanzarnos
Python al momento de ejecutar un programa!

    ¿Qué estamos haciendo?
    ¿Qué error nos está dando?
    ¿Qué podemos hacer?
    ¿Cómo interpretar el error que vemos en la consola?

"""

#### --> SyntaxError: Cuándo nos equivocamos en la escritura del código!
##       puede ser una sola letra, signo o palabra entera. El interprete
##       ya nos indica este error.
# print "Hola!" # Error
print("Hola <3") # Correcto

#### --> NameError: sucede cuándo queremos llamar a una variable que no
##       está definida, recordemos que incluso el lenguaje es sensible a
##       mayúsculas y minúsculas.
# print(resultado) # error
resultado = 10 + 10
print(resultado) # correcto!

#### --> IndexError: cuándo el sistema trata de buscar el índice de un 
##       elemento que NO está existente, fuera del rango. Por ejemplo,
##       de una lista de 4 elementos, no se podría acceder al 6.
##       este me sale muchísimo en estos días lol
my_list = ["Java", "JavaScript", "LabVIEW", "Python", "C#", "C++"]
# print(f"Elemento: {my_list[10]}") # Error
print(f"Elemento: {my_list[2]}")

#### --> ModuleNotFoundError: cuándo el sistema busca llamar un modulo
##       que NO existe!
# import maths # Error
import math # Correcto!

#### --> AttributeError: cuándo el sistema busca llamar a un atributo
##       inexistente o mal escrito.
# print(math.PI) # Error
print(math.pi) # Correcto!
print(f"Métodos en math: \n{dir(math)}")

#### --> KeyError: cuándo el sistema quiere llamar a una clave (key) que
##       no existe o está mal escrita
my_dict = {
    "Name" : "Fanny",
    "Surname" : "Guerrero",
    "Profession" : "Ingeniera en computación",
    "Languages" : ["Java", "Python", "JavaScript"]
}
# print(f"Elemento: {my_dict["Edad"]}") # Error
print(f"Elemento: {my_dict['Languages']}") # Correcto!

#### --> TypeError: cuándo queremos hacer uso de un tipo de dato diferente
##       a lo establecido, por ejemplo, si queremos acceder a elementos en 
##       una lista usando una key de diccionario (list != dict)
# print(f"Elemento de lista: {my_list["Nombre"]}") # Error

#### --> ImportError: cuándo se intenta acceder a elementos que no están
##       disponibles en una librería/modulo.
# from math import PI # Error!
from math import pi # Correcto!
print(f"Valor de pi: {pi}")

#### --> ValueError: si se quiere pasar un elemento de un valor, digamos str
##       a int, a otro que no le corresponde.
# my_number = int("10 años") # Error!
# print(my_number)

#### --> ZeroDivisionError: cuándo se busca dividir entre 0
# print(f"División entre 0: {4/0}") # Error