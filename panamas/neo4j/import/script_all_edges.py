#!/usr/bin/python

import csv

edges = open('all_edges.csv', 'rb')
edgescsv = csv.reader(edges, delimiter=',')
liste = []
for row in edgescsv:
    row = [col.lower() for col in row]
    if not row[1] in liste:
        liste.append(row[1])
        
liste.pop(0)
liste.sort()
print (liste)
print (len(liste))
edges.close()

            
