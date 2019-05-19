##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

col1 = [str(row[0]) for row in tabla]
#print (col1)
values = set(col1)
values = list(values)#.sort()
values.sort()
#print (values)

salida = [(vocal,col1.count(vocal)) for vocal in values]
for i,j in salida:
    print ("{},{}".format(i,j))