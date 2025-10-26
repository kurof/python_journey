"""__summary__

Día 14 del reto de 30 días de Python, la lección de hoy es: Funciones
de Grado Superior.
En Python, las funciones son tratadas como "ciudadanos de primera
clase", perimitiendonos hacer algunas de las siguientes operaciones:

    - Una función puede tomar uno o más funciones como parámetros.
    - Una función puede ser devuelta como resultado de otra función.
    - Una función puede ser modificada.
    - Una función se puede asignar a una variable.

Los siguientes ejercicios se enfocarán en:
    1. Manejar funciones como parámetros.
    2. Regresar funciones como valor de retorno de otra función.
    3. Usar closures y decoradores de Python.

** Closures -> Python permite a funciones anidadas acceder al scope
               de la función superior. Se crea al anidar una función
               dentro de otra, encapsulando la función y regresando
               la función interna (es algo confuso pero se devuelve
               la función de adentro)

** Decorators -> Un decorator, en Python, permite a un usuario agregar
                 una nueva funcionalidad a un objeto existente sin
                 modificar su estructura. Usualmente se llaman antes
                 de la definición que se quiera decorar.
                 - Para crear una función decorada, necesitamos una 
                   función externa con una función interna anidada.

Reto original: Asabeneh
Tutoriales: MoureDev
"""

##### EJERCICIOS DEL DIA 14

from functools import reduce


print("------ FUNCIONES DE GRADO SUPERIOR ------")

### --> Listas con las que se va a trabajar
countries = ["Estonia", "Finlandia", "Suecia", "Dinamarca", "Noruega", "Islandia"]
names = ["Fanny", "Agatha", "Garreth", "Vitani", "Ofir", "Ashara"]
numbers = [1,2,3,4,5,6,7,8,9,10]

# agregando lista de asabeneh
extended_countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#### --> Ejercicios de nivel 1
print("\n--> Ejercicios de nivel 1")
## -> Usando for para imprimir elementos
print("\n--- Países con for ---")
for country in countries:
    print("- ",country)

print("\n--- Nombres con for ---")
for name in names:
    print("+", name)

print("\n--- Números con for ---")
for num in numbers:
    print(num)

#### --> Ejercicios de nivel 2
## -> Usando map para crear una lista de países en mayusculas
def to_upper(element): # para evitar repetir la lambda
    return element.upper()

new_countries_list = list(map(to_upper, countries))
print(f"\nPaíses en mayúsculas: \n{new_countries_list}")

## -> Usando map para cambiar cada numero a su cuadrado
new_numbers_list = list(map(lambda n: n**2, numbers))
print(f"\nNúmeros al cuadrado: \n{new_numbers_list}")

## -> Usando map para cambiar a mayusculas los nombres
new_names_list = list(map(to_upper, names))
print(f"\nNombres en mayúscula: \n{new_names_list}")

## -> Usando filter para filtrar los países que terminen en "landia"
ends_w_land = list(filter(lambda country: country.endswith("landia"), countries))
print(f"\nPaíses que terminan con \"landia\": \n{ends_w_land}")

## -> Usando filter para paises con 6 caracteres
six_characters = list(filter(lambda country: len(country) == 6, countries))
print(f"\nPaíses de 6 caracteres: \n{six_characters}")

## -> Usando más de una función de grado superior del sistema
chaining = list(filter(lambda country: country.startswith("E"), map(to_upper, countries)))
print(chaining)

## -> Haciendo una lista con muchos elementos y haciendo funcion que devuelva string
fused_list = names + numbers # fusionando nombres y numeros

def get_string_list(lst):
    string_only = [item for item in lst if type(item) == str]
    return string_only
        
print(f"Lista fusionada: \n{fused_list}")
print(f"Solo strings: \n{get_string_list(fused_list)}")

## -> Usando reduce para sumar todos los elementos en numeros
num_sum = reduce(lambda a,b : a + b, numbers)
print(f"\nSumando elementos de numbers: \n{num_sum}")

## -> Usando reduce para juntar todos los paises
countries_string = reduce(lambda c1, c2 : c1 + ", " + c2, countries) + " son nordicos"
print(f"\nConcatenación: \n{countries_string}")

## -> Creando una función que regrese un diccionario donde keys sea la inicial
##    del país y el valor, la cantidad de palabras que inician con ella
def counting_initials(lst):
    # obteniendo iniciales
    initials = [country[0] for country in lst]

    # creando un diccionario
    initials_dict = {
        initial : initials.count(initial) 
        for initial in set(initials) # set para que no se repitan!
    }

    return initials_dict # devolvemos el diccionario
    
print(f"Diccionario de conteo de iniciales: \n{counting_initials(extended_countries)}")

## -> Declara una función que obtenga los primeros 10 países de extended_countries
def get_first_ten(countries_lst):
    first_ten = []
    # contando hasta 10
    for i in range(0,10):
        first_ten.append(countries_lst[i])
    return first_ten

print(f"\nPrimeros 10 elementos: \n{get_first_ten(extended_countries)}")

## -> Regresa los ultimos 10 elementos de extended_countries
def get_last_ten(countries_lst):
    lst_len = len(countries_lst)-1 # restando 1 para que no pase del tamaño de la lista
    last_ten = [] # lista para guardar los elementos

    # recorriendo lista, desde el punto máximos y vamos hacia atras (-1)
    for element in range(lst_len, 0, -1):
        last_ten.append(countries_lst[element]) # agregamos el elemento

        # si la iteracion llega al 10, se acaba
        if element == (lst_len-11):
            break
    return last_ten

print(f"\nImprimiendo los ultimos 10: \n{get_last_ten(extended_countries)}")