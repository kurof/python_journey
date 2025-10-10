"""__summary__

La lección de hoy son: dates, fechas, características de
tiempo. Siempre hay un momento en el que tal vez haya
que trabajar con fechas; si bien es algo común, no es
como un string u otro tipo de dato dentro de Python! Aquí
es necesario hacer la importación de su modulo correspon-
diente.

Usualmente contienen la fecha, hora, etc; dates o fechas
son objetos complejos que están encapsulados para ello,
es decir, tiene muchos métodos que nos permiten trabajar
con fechas y horas (siento que es mucho texto sorry)
"""

from datetime import datetime, time, date, timedelta

# creando una fecha (usando metodo now)
now = datetime.now()
print(f"Fecha de hoy: {now}")

# usando otras propiedades de nuestra variable now
print(f"Día actual: {now.day}")
print(f"Mes: {now.month}")
print(f"Año: {now.year}")

# usando timestamp, una representación única de un momento justo
# formato POSIX, esto podemos usarlo si es necesario convertir
# la fecha, usando una llamada a API y hacerlo de forma
# más simple, ya que si lo hacemos de una forma más comprensible
# para nosotros... será un objeto muy complejo para el programa!
# Es un estandar!
ts = now.timestamp()
print(ts)

# ya vimos como hacer un stamp del momento exacto de ejecucion, 
# pero... y si queremos trabajar con una fecha diferente? A veces,
# es importante si trabajamos con servidores y BD que quizás 
# tengan usuarios que no están en el mismo país en el que estamos
# en fin, vamos a  intentar otro tipo de datetime!
year_2026 = datetime(2026,1,1)

# funcion usando fecha
def current_year(d):
    print("\n--- Fecha actual ---")
    print(f"Año actual --> {d.year}")
    print(f"Mes actual --> {d.month}")
    print(f"Día actual --> {d.day}")
    print(f"Timestamp --> {d.timestamp()}")

current_year(now)
current_year(year_2026)

#### Vamos a usar time, de datetime (ambas son similares
# pero diferentes!)
time_now = time()
print(f"Tiempo actual: {time_now.hour}")

# La parte de arriba no devolverá algo porque time() es algo que
# no contiene información como datetime; aquí tendríamos que 
# hacer ciertas operaciones. Time es un objeto para encapsular tiempo,
# nosotros debemos darle valor
time_now = time(15, 23, 00) # ejemplo
print(time_now)

#### Usando date
date_now = date(2025,10,6) # debemos ponerle argumentos
print(f"Fecha original: {date_now}") 

#### Operaciones con fechas
print(date_now.isoweekday()) # nos regresa que dia es hoy (lunes = 1)
print(date_now.today()) # imprime la fecha que tiene almacenada

# no es realmente posible o aconsejable, editar elementos de un date, pero
# es posible (estamos reinstanciando):
# De todos modos: es posible restar o sumar fechas, siempre y cuándo sean 
# del mismo tipo (si son 2 elementos de tipo de date, pero no en time)
date_now = date(
    date_now.year, date_now.month + 1, date_now.day +1
)

print(f"Fecha alterada: {date_now}")

#### Usando timedelta! que es una clase que nos permite hacer operaciones
# aritmeticas entre objetos de tiempo, como sumar, restar, etc. Podemos 
# meter muchos valores como horas, minutos, días, semanas, etc.
# Timedelta NO es para trabajar con fechas, es para trabajar con ciertos
# rangos de tiempo, para calcular espacios de tiempo (por ejemplo, nos 
# ayuda a hacer un calculo de tiempos de suscripción de un usuario,
# cuánto tiempo tienen de suscripción y así)

# para hacer una operación, haremos 2 valores
time_delta_ini = timedelta(200,10,100,weeks=10)
time_delta_end = timedelta(300, 100,100,weeks=13)

print("\n---- Usando timedelta ----")
print(f"\nTimedelta inicial -> {time_delta_ini}")
print(f"Timedelta final -> {time_delta_end}")
print("\n---- Operaciones con timedelta ----")
print(f"Diferencia entre ini y end -> {time_delta_end - time_delta_ini}")
print(f"Suma de ini y end -> {time_delta_ini + time_delta_end}")
# no se puede multiplicar
print(f"Dividiendo ini y end -> {time_delta_ini / time_delta_end}")