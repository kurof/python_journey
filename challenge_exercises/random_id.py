## Modulo para generar nombre de usuario de 6 digitos
# - letras
# - numeros

from random import choice
from string import ascii_letters, digits
from math import ceil

# funcion para generar
def random_user_id(chars : int):
    
    # variable de id
    generated_id = ""
    numbers_digits = ascii_letters + digits

    # loop
    for char in range(1,chars+1):
        generated_id += choice(numbers_digits)

    return generated_id

def user_id_gen_by_user(chars : int, number_ids : int):
    # para guardar la lista
    id_list = []

    # loop para guardar los elementos
    for i in range(0, number_ids):
        id_list.insert(i, random_user_id(chars))
    return id_list