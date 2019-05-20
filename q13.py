##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

tabla1 = [(i[0],i[4].split(',')) for i in tabla]
"""
tabla2 =  []
for linea in tabla1:
    temp = tuple()
    print(linea[0])
    for codigo in linea[1]:
        suma=0
        suma = suma +int(codigo[-1])
        print (suma)
"""
for linea in tabla1:
    salida = [(linea[0],codigo[-1]) for codigo in linea[1] for linea in tabla1]

print (salida)