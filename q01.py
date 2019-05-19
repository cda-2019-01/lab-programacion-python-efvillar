##
## Imprima la suma de la segunda columna.
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

#print(len(tabla))
#print(tabla[0])
col2 = [int(row[1]) for row in tabla]
print(sum(col2))