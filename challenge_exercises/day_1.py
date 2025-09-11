"""_summary_
Ejercicios del desafío de 30 días de codificación Python!
Los siguientes ejercicios serán en nivel 1, esto irá avanzando
más y más de dificultad.
Este archivo contiene el ejercicio de nivel 3 del desafío:
encontrar la distancia Euclidiana (?) entre:
    - a(2,3)
    - b(10,8)

    Formula: d(p,q) = raiz((p1 - q1)² + (p2 - q2)²)
Desafío original: Asabeneh
Tutoriales: MoureDev
"""

#operacion
import math

#Este es un gran y enorme: creo que está bien así
distancia_euclidiana = math.sqrt((2-10)**2 + (3-8)**2)
print("Distancia entre los puntos: \n(2,3) y (10,8)")
print(f"--> {round(distancia_euclidiana, 2)}")
print(type(distancia_euclidiana))
# print(f"a{punto_1}, b{punto_2}")