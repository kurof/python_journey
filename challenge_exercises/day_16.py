"""Nota-> El día 15 es sobre tipos de errores en Python, así que se
          salta y pasamos al día 16

    Día 16 del reto Python, la lección de hoy es: Datetime.
    Python contiene un modulo para manejar las fechas y hacer 
    operaciones con esto; el enfoque principal de las funciones de 
    este modulo serán:

        - date
        - datetime
        - time
        - timedelta

Reto original: Asabeneh
Tutoriales: MoureDev
"""

## -> Obten el día, mes, año, hora, minuto y timestamp actuales con 
##    el modulo datetime
from datetime import date, datetime

# variables
today = datetime.now() # hoy

day = today.day
month = today.month
year = today.year
hour = today.hour
minutes = today.minute
time_stamp = today.timestamp()

print(f"Fecha: {day}/{month}/{year} \nHora: {hour}:{minutes} \nTimestamp: {time_stamp}")

## -> Formatea la fecha con el siguiente formato: %m/%d/%Y, %H:%M:%S
# usando strftime (usamos la variable today)
t_formatted = today.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formato strftime: {t_formatted}")

## -> Cambia la fecha actual (presentada en string) a date
current_date = "25 October, 2025"
# para convertir, hay que usar la misma forma del string!
current_date_time = datetime.strptime(current_date, "%d %B, %Y") 

print(f"\nString original: {current_date}")
print(f"String a date: {current_date_time}")

## -> Calcula la diferencia de tiempo entre ahora y año nuevo (date)
today = date(2025,10,25)
new_year = date(2026,1,1)

date_diff = new_year - today
print(f"Días restantes para año nuevo: {date_diff}")

## -> Calcula la diferencia entre el 1 de Enero de 1970 y hoy
first_date = date(1970,1,1)

date_diff = today - first_date
print(f"Diferencia entre 1970 y hoy: {date_diff}")

## -> Piensa: cuáles podrían ser los usos que podemos darle al modulo
##            datetime? Hay algunos ejemplo como: análisis de tiempo,
##            obtener el timestamp de una aplicación, ver qué 
##            actividades se han hecho en la aplicación, o añadir posts
##            a un blog.
##            Creo que podría usarse también para manipular los 
##            reproductores de video, saber el tiempo que dura, si se 
##            manipula para ir a un punto específico, para compartir
##            un punto específico del video, entre otras cosas!