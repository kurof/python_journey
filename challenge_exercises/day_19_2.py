######## PROCESANDO ARCHIVOS CSV
import csv

## --> Trabajando con un archivo csv, con el archivo hacker_news.csv y:
#           1. Cuenta el número de líneas que tengan la palabra Python o python
#           2. Cuenta las líneas que contengan JavaScript, javascript o Javascript
#           3. Cuenta las líneas que contengan Java (no JavaScript)
def reading_csv(csv_path, word):

    with open(csv_path) as csv_f:
        csv_reader = csv.reader(csv_f, delimiter= ",")
        csv_to_str = ""
        counter = 0

        # agregando elementos a un elemento string
        for row in csv_reader:
            csv_to_str = csv_to_str + ", ".join(row)

        # poniendo elementos a minusculas
        csv_to_list = csv_to_str.lower().split()

        # buscando la palabra dentro del nuevo string
        for w in csv_to_list:
            # si la palabra está ahí, aumentamos el contador
            if w == word:
                print(w)
                counter += 1
        
    return f"Aparición de {word}: {counter}"

# Usando la función
file_c = "challenge_exercises/hacker_news.csv"
word_p = "python"
word_js = "JavaScript"
word_j = "Java"


print(reading_csv(file_c, word_p.lower()))