""" Operaciones que se pueden hacer sobre una lista de números,
paquete hecho para los ejercicios del día 20 del challenge python
(archivo day_20.py) """

from statistics import mean, median, stdev


def minimum_value(num_list):
    return f"Elemento mínimo: {min(num_list)}"

def maximum_value(num_list):
    return f"Elemento máximo: {max(num_list)}"

def info_mean(num_list):
    return f"Promedio: {round(mean(num_list),1)}"

def info_median(num_list):
    return f"Mediana: {round(median(num_list),1)}"

def info_standard_dev(num_list):
    return f"Standard deviation: {round(stdev(num_list),1)}"