##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

col1 = [str(row[0]) for row in tabla]
values = set(col1)
values = list(values)#.sort()
values.sort()
#print (values)

#print type(tabla[1][1])

input = [(tabla[i][0],int(tabla[i][1])) for i in range(len(tabla))]
#print (input)

for v in values:
    suma = (v,sum([item[1] for item in input if item[0]==v]))
    print ('{},{}'.format(suma[0],suma[1]))