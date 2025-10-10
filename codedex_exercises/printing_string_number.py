# recibiendo elemento
print("--- Imprimiendo un string con n numeros ---")
n = int(input())
number_string = ""

# loop to print
for i in range(1,n+1):
    number_string += str(i)

print(number_string)

# procesando un string y viendo si es alfanumerico, está
# ordenado alfabeticamente, digitos, en minusculas o
# mayusculas
print("\n--- Viendo qué tipo de string hemos puesto ---")
s = input()

# procesando (para el ejercicio, se debe checar caracter por caracter)
print(any(letter.isalnum() for letter in s)) # buscando elementos alfanumericos en cadena
print(any(letter.isalpha() for letter in s))
print(any(letter.isdigit() for letter in s))
print(any(letter.islower() for letter in s))
print(any(letter.isupper() for letter in s))