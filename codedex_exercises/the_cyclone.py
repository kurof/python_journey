# variables para almacenar
height = float(input("¿Cuál es tu altura? "))
current_credits = int(input("Créditos disponibles: "))

# evaluando
if height >= 1.37 and current_credits >= 10:
    print("Puedes subir a los juegos :D")
elif height >= 1.37 and current_credits < 10:
    print("No tienes suficientes créditos")
elif height < 1.37 and current_credits >= 10:
    print("No cumples con la altura mínima")
else:
    print("No cumples con ninguno de los requisitos")