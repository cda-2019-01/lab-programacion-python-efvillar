##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

colA = [row[2] for row in tabla]
colB = [data[5:7] for data in colA]

#print (colB)


#col1 = [str(row[0]) for row in tabla]
#print (col1)
values = set(colB)
values = list(values)#.sort()
values.sort()
#print (values)

salida = [(vocal,colB.count(vocal)) for vocal in values]
for i,j in salida:
    print ("{},{}".format(i,j))
