"""
Modulo para la generación de colores rgb, la función
rgb_color_gen generará un color basado en 3 valores 
que van desde el 0 al 255
"""

# importando random para valores aleatorios
from random import choice, randint

def rgb_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    print(f"rbg({r},{g},{b})")

# para generar colores hexadecimales
# compuesto por: 
#   - numeros (0-9)
#   - 6 letras (a-f)
def generating_hexa_color():
    color = "#"
    chars = "abcdef0123456789"

    # loop
    for color_char in range(1,7):
        color += choice(chars)
    return color

# generando lista de hexadecimales
def list_of_hexa_colors(n : int):
    # lista
    colores = []

    #loop
    for i in range(0, n):
        colores.insert(i, generating_hexa_color())
    return colores