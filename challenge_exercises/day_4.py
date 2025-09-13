"""__summary__
Día 4 del desafío de Python; en este archivo están algunos 
de los ejercicios del repositorio GitHub del desafío y el
tema central es: STRINGS.

Reto original: Asabeneh
Tutoriales: MoureDev
"""

# --> Concatenando strings (por cierto, mis variables no deberian nombrarse asi lol)
# a, b, c, d = "Thirty", "days", "of", "Python"
# message_concatenated = f"{a} {b} {c} {d}"
# print(message_concatenated)

a2, b2, c2 = "Coding", "for", "All"
message_for_you = f"{a2} {b2} {c2}"
company = message_for_you

print(f"Mensaje original: {company}")
print(f"Tamaño: {len(company)}")

print(f"En mayúsculas: {company.upper()}")
print(f"En minúsculas: {company.lower()}")
print(f"La primera letra mayúscula: {company.capitalize()}")
print(f"Primera letra de cada palabra mayúscula: {company.title()}")
print(f"Invirtiendo mayúsculas y minúsculas: {company.swapcase()}")
print(f"Quitando \"Coding\": {company.strip("Coding")}")
print(f"¿Índice de \"Coding\"? {company.index("Coding")}")

print(f"Reemplazando coding: {company.replace("Coding", "Python")}")
print(f"Partiendo el string: {company.split(" ")}")
print(f"Caracter en 0: {company[0], company[-1], company[10]}") # -1 caracter al final
print(f"Caracter donde aparece primero una C: {company.index("C")}")
print(f"Última aparición de de \"l\": {company.rfind("l")}")

# --> Otro string
actual_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(f"\nMensaje original: {actual_companies}")
print(f"Dividiendo: {actual_companies.split(", ")}")

# --> Usando el método isidentifier()
print("\n¿Es un nombre de variable valido?")
print(f"30DaysOfPython -> {"30DaysOfPython".isidentifier()}")
print(f"thirty_days_of_python -> {"thirty_days_of_python".isidentifier()}")

# --> Haciendo un lista y haciendo join
python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(f"Juntando una lista: {" - ".join(python_libraries)}")

# --> Dando formato a algunos elementos
print("\nName \tAge \tCountry \tCity")
print("Fanny \t28 \tMéxico \t\tQuerétaro")