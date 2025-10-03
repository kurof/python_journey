"""__summary__
La siguiente lección es: Manejo de Excepciones (o Exceptions).
La premisa es simple: si nos sale un error en nuestro código,
y no lo manejamos... nuestro programa se detendrá!
Los errores siempre van a salir, es algo normal y parte de la
vida, pero debemos aprender a manejar estos errores para que
nuestro programa continue funcionando.

En Python, el manejo de errores se hace a través del bloque
"try" (try-catch en java), el cual:
    - Intenta ejecutar un segmento de código
    - Si falla, pasa a un bloque llamado "except" (que puede
      o no tener una condición adicional), que indica otro
      segmento de instrucciones a ejecutar
    - SI NO HAY EXCEPCION, pasa a un else que ejecuta otro
      código.
    - Y pasamos al bloque finally, que sí o sí ejecuta 
      un código

    Nota: no es lo mismo que un if-else
"""

# Ejemplo de una excepcion
number_one = 5
number_two = 1

number_two = "10" # cambiando a un string (dará una excepción)

# imprimiendo operacion
# print(number_one + number_two)

# usando try-except para manejar el error
try:
    print(number_one + number_two)
    print("Sin errores ;D")
except: # si ocurre un error, ponemos esto
    print("Ha ocurrido un error de tipado")
else: # esto es OPCIONAL
    print("El código se sigue ejecutando")
    # esto se ejecuta solo si el except no se cumple!
finally: # también es opcional
    print("El programa sigue corriendo :o")
    # esto se ejecuta sí o sí! 

## Capturando una excepción por tipo!
try:
    print(number_one + number_two)
    print("Sin errores ;D")
except TypeError as e: # poniendo el tipo de error que dará
    print("Excepción de tipo TypeError")
except ValueError: # se puede poner más de un tipo de excepción!
    print("Excepción de tipo ValueError")

# Capturando una excepción y la información de la misma!
try:
    print(number_one + number_two)
    print("Sin errores ;D")
except TypeError as e: # si ocurre un error, ponemos esto
    print(f"Info: {e}")
    # esta información se puede pasar a algun programa como
    # firebase, o un log para registro, etc.
except Exception as e:
    # podemos agregar una excepcion generica, si no sabemos el tipo de error
    print(f"Info: {e}")