#!/usr/bin/python

import csv

edges = open('all_edges.csv', 'rb')
edgescsv = csv.reader(edges, delimiter=',')
liste = []
for row in edgescsv:
    row = [col.lower() for col in row]
    row = [col.strip() for col in row]
    if not row[1] in liste:
        liste.append(row[1])

liste
edges.close()


with open('all_edges.csv', 'rb') as edges_file:
    reader = csv.DictReader(edges_file)
    data = {}
    for row in reader:
        for header , values in row.items():
            
