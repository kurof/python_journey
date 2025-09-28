## --> Planet dictionary
planets = {
    "Mercurio" : 0.38,
    "Venus" : 0.91,
    "Marte" : 0.38,
    "Jupiter" : 2.53,
    "Saturno" : 1.07,
    "Urano" : 0.89,
    "Neptuno" : 1.14
}

# --> Input variables
earth_weight = float(input("Peso (en la Tierra) en kg: "))
number_planet = 0
destination_weight = 0

print("\nEscoge un planeta:" \
"\n1) Mercurio \n2) Venus \n3) Marte \n4) Jupiter" \
"\n5) Saturno \n6) Urano \n7) Neptuno")
number_planet = int(input("\n")) # we put the input here!

## --> Processing answers
if number_planet == 1:
    destination_weight = earth_weight * planets["Mercurio"]
elif number_planet == 2:
    destination_weight = earth_weight * planets["Venus"]
elif number_planet == 3:
    destination_weight = earth_weight * planets["Marte"]
elif number_planet == 4:
    destination_weight = earth_weight * planets["Jupiter"]
elif number_planet == 5:
    destination_weight = earth_weight * planets["Saturno"]
elif number_planet == 6:
    destination_weight = earth_weight * planets["Urano"]
elif number_planet == 7:
    destination_weight = earth_weight * planets["Neptuno"]
else:
    print("Invalid planet")

print(f"Peso en otro planeta: {round(destination_weight, 2)}")