"""
Código para convertir las siguientes divisas:
  - Pesos colombianos
  - Soles peruanos
  - Reais brasileños
A USD, o sea, dolares, se le pedirá al usuario input
"""

print("--- Conversion de divisas ---")

peso_col = float(input("Cantidad de pesos colombianos: "))
sol_per = float(input("Cantidad de soles peruanos: "))
reais_br = float(input("Cantidad de reales brasileños: "))

# calculando cuanto es en USD
# cantidades del 9 sept 2025
col_usd = round(peso_col / 3922.87, 2)
sol_usd = round(sol_per / 3.50, 2)
real_usd = round(reais_br / 5.43, 2)

total_usd = round(col_usd + sol_usd + real_usd)

print(f"Total USD: $ {total_usd}")