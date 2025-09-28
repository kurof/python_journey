# Write code below 💖
# Sorting Hat <|:)

# house variables (all start on 0)
# hufflepuff, slytherin, ravenclaw, griffindor = 0, 0, 0, 0

houses = {
    "Hufflepuff" : 0,
    "Slytherin" : 0,
    "Ravenclaw" : 0,
    "Griffindor" : 0
}

# questions (user inputs)
q1 = int(input("¿Qué prefieres? \n1) Amanecer \n2) Atardecer \n"))

q2 = int(input("Cuándo muera, quiero que la gente me recuerde como:\n1) El Bueno \n2) El Grande \n3) El Sabio \n4) El Impulso\n"))

q3 = int(input("¿Qué instrumento prefieres? \n1) Violín \n2) Trompeta \n3) Piano \n4) Tambor\n"))

# processing answers
# question  1
if q1 == 1:
    houses["Griffindor"] += 1
    houses["Ravenclaw"] += 1
elif q1 == 2:
    houses["Hufflepuff"] += 1
    houses["Slytherin"] += 1
else:
    print("Opción incorrecta!")

# question 2
if q2 == 1:
    houses["Hufflepuff"] += 2 # sumamos 2 al elemento actual
elif q2 == 2:
    houses["Slytherin"] += 2
elif q2 == 3:
    houses["Ravenclaw"] += 2
elif q2 == 4:
    houses["Griffindor"] += 2
else:
    print("Opción no válida")

# question 3
if q3 == 1:
    houses["Slytherin"] += 4
elif q3 == 2:
    houses["Hufflepuff"] += 4
elif q3 == 3:
    houses["Ravenclaw"] += 4
elif q3 == 4:
    houses["Griffindor"] += 4
else:
    print("Opción inválida")

# printing results
print(houses)
final_house = max(houses) # getting the house (max results)

print(f"Tu casa Hogwarts es: {final_house}")