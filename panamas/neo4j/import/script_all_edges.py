#!/usr/bin/python

import csv


liste = []
new_rows_list = []

with open("all_edges.csv", "r") as edges_reader:
    reader = csv.reader(edges_reader, delimiter=',')
    for row in reader:
        #passer le premier label des headers
        if reader.line_num == 1:
            new_rows_list.append(row)
            continue
        row = [col.lower() for col in row]
        r = row[1]
        if "/" in r:
            r = r.split("/")[0]
        #if "of" in r :
        #    r = r.split("of")[0]
        if "&" in r :
            r = r.split("&")[0]
        r = r.strip()
        row[1] = r
        new_rows_list.append(row)
        if not r in liste:
            print (r)
            liste.append(r)

edges_reader.close()

liste.sort()
print (liste)
print (len(liste))

with open("all_edges.csv","w") as edges_writer:
            writer = csv.writer(edges_writer, delimiter=',')
            writer.writerows(new_rows_list)
edges_writer.close()


type_row_list = []
with open("all_edges.csv","r") as edges_reader :
    reader = csv.reader(edges_reader, delimiter=',')
    for row in reader :
        if row[1] in liste :
            type_row_list.append(row)
for l in liste:
    outfilename = "egdes_{}.csv".format(l)
    with open(outfilename, "a") as outfile:
        edge_writer = csv.writer(outfile)
        for row in edgescsv_reader:
            if l == row[1]:
                edge_writer.writerow(row)
outfile.close()
        


edges_reader.close()

            
