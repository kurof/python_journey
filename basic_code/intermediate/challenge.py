### retos de programación de MoureDev
""" FizzBuzz:
 -> Multiplos de 3 y 5, imprime FizzBuzz
 -> Multiplos de 5, imprime Buzz
 -> Multiplos de 3, imprime Fizz
"""
def fizzbuzz():
    print("---- FizzBuzz ----")
    #loop de los numeros 1-100
    for i in range(1,101):
        # condiciones
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)

fizzbuzz() # llamando a funcion

"""
 Es un anagrama?
 Escribe una función que reciba 2 palabras (string) y retorne verdadero
 o false (bool) según sea o no un anagrama.
    - Un anagrama consiste en formar una palabra reordenando TODAS las
      letras de otra palabra inicial.
    - NO hace falta verificar que ambas palabras existan
    - Dos palabras exactamente iguales NO son anagramas.
"""
def isanagram(word1 : str, word2 : str):
    print("\n---- ¿Es una Anagrama? ----") 
    # pasando a minusculas
    word1, word2 = word1.lower(), word2.lower()

    # procesando los argumentos (los pasamos a minusculas)
    if word1 == word2:
        print(f"Es la misma palabra, por lo tanto: {False}")
    else:
        # ordenamos las letras en una lista (sorted) y comparamos
        print(f"Las palabras son anagramas: {sorted(word1) == sorted(word2)}")

isanagram("Amor", "roma")

"""
 Sucesión de Fibonacci
 Escribe un programa que imprima los 50 primeros números de la sucesión 
 de Fibonacci empezando del 0. 
    - La serie Fibonacci se compone por una sucesión de números en la
      que el siguiente siempre es la suma de los dos anteriores. Algo
      como:
        [0,1,1,2,3,5,8,13,...]
"""
def fibonacci():
    print("\n---- Sucesión de Fibonacci ----")

    # variable para almacenar
    prev_num = 0
    next_num = 1

    # usando un for para imprimir
    for i in range(1,51):
        print(prev_num)

        fib = prev_num + next_num # calculo de fibonacci
        prev_num = next_num # el numero anterior se hace el siguiente
        next_num = fib # el siguiente numero es la suma de fibonacci

fibonacci()

"""
 ¿Es un número primo?
 Escribe un programa que se encargue de comprobar si un número es o no
 primo. Hecho esto, imprime los números primos entre 1 y 100.
"""
def isprime():
    
    for number in range(1,101):
        if number >= 2:

            # divisible
            is_divisible = False

            for i in range(2,number):
                if number % i == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)
        
isprime()

"""
 Crea un programa que invierta el orden de una cadena de texto
 sin usar funciones propias del lenguaje (aquellas que lo hacen de
 forma automática).
    - Si pasamos algo como: "Hola Mundo", nos debería regresar algo como:
      "odnum aloh"
"""

def reverse_string(frase : str):
    reversed_text = ""
    text_len = len(frase)
    
    # iterando texto que llega
    for letter in range(0, len(frase)): # yendo hacia atras
        reversed_text += frase[text_len - letter -1]

    return reversed_text

print(reverse_string("Hola mundo"))