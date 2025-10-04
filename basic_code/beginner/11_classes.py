"""_summary_

Una clase nos sirve para crear un objeto; todo lo que está 
dentro de una clase debe tener sentido y lógica con el tipo
de objeto que hacemos. Por ejemplo, si hacemos una clase
persona, deberemos poner elementos que correspondan a una
persona, no podemos agregar cosas como: "volar" o "tipo de
cola" ya que eso no se relaciona al tipo de objeto que 
estamos creando.

Para crear una clase, usamos la palabra reservada "class", 
seguida del nombre que queramos ponerle a nuestra clase.
    Nota: Los nombres de una clase se escriben con
          camel case, es decir, la primera letra de cada
          palabra en mayúscula (ej: MyClass)

Una clase puede tener constructores, que nuestra clase 
pueda hacer cosas! Esto se hace a través de la función
__init__, que es para hacer un constructor en Python que
sea capaz de recibir parámetros.
Lo mejor es tener nuestros propios ficheros para almacenar
nuestras clases.

Para poner variables privadas, usamos __nombre y para acceder
a estos elementos, al igual que en java o cualquier POO, 
hacemos un getter y para editarlos un setter
"""

### Definiendo una clase
class MyEmptyPerson:
    pass # palabra de relleno para que no de error

# --> Otra clase con parámetros
class MyPerson:
    # método init, constructor en Python
    def __init__(self, name, surname, alias = "NA"):
        # self, refiriendose a la clase en la que estamos
        # asignamos los parametros o elementos de la persona
        # es obligatorio de los constructores
        # Todo lo que esta declarado con self
        # self.nombre = name # nombre será la forma en la que accedemos!
        # self.surname = surname
        self.fullname = f"{name} {surname} alias: {alias}" # propiedad pública

        self.__name = name # privado
        self.__surname = surname # privado
    
    # getter para nombre (ojo: solo lectura, no se edita)
    def get_name (self):
        return self.__name # devolviendo nombre, se debe llamar a esta funcion

    # funciones propias de la clase (para hacer objetos)
    # tenemo que referenciar a la misma clase, self, en la que está
    def walk(self):
        print(f"{self.fullname} is walking -->")

# Usando nuestra clase (instanciando clase!)
my_person = MyPerson("Fanny", "GM")
print(my_person.fullname)
my_person.walk() # llamando a una funcion/metodo
# print(my_person.nombre, my_person.surname)

my_other_person = MyPerson("Agatha", "Surana")
print(my_other_person.fullname)
# sobreescribiendo fullname, esto se puede hacer
my_other_person.fullname = "Agatha Surana, Heroína de Ferelden"
print(my_other_person.fullname)

print(my_person.get_name()) # usando el getter