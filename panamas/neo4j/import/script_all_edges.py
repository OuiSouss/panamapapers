#!/usr/bin/python

import csv
import os.path

global row_header

global liste
global new_row_list

new_row_list = []
liste =[]
row_header = ['node_1','rel_type','node_2','sourceID','valid_until','start_date','end_date']

def read_and_reformate():
    with open("all_edges.csv", "r") as edges_reader:
        reader = csv.reader(edges_reader, delimiter=',', lineterminator='\n')
        
        for row in reader:
            #passer le premier label des headers
            if reader.line_num == 1:
                continue

            row = [col.lower() for col in row]
            r = row[1]
            
                
            r = r.strip()
            row[1] = r
            new_row_list.append(row)
            if not r in liste:
                print (r)
                liste.append(r)
    edges_reader.close()

def read():
    l = []
    with open("all_edges.csv", "r") as edges_reader:
        reader = csv.reader(edges_reader, delimiter=',', lineterminator='\n')
        
        for row in reader:
            if reader.line_num == 1:
                continue
            r = row[1]
            if not r in l:
                l.append(r)
    edges_reader.close()
    return l



def write_reformating():
    with open("all_edges.csv","w") as edges_writer:
        writer = csv.writer(edges_writer, delimiter=',', lineterminator='\n')
        writer.writerow(row_header)
        writer.writerows(new_row_list)
    edges_writer.close()

global name_type_act

def create_children_files():
    while liste != []:
        type_row_list = []
        name_type_act = liste[0]
        with open("all_edges.csv","r") as reader:
            read = csv.reader(reader, delimiter=',', lineterminator='\n')
            for row in read :
                if row[1] == name_type_act and row[1] in liste :
                    type_row_list.append(row)
        reader.close()

        outfilename = "edges_{}.csv".format(name_type_act)
        if os.path.isfile(outfilename) == False:
            with open(outfilename, "a") as outfile:
                writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
                writer.writerow(row_header)
                writer.writerows(type_row_list)
            outfile.close()
        liste.remove(name_type_act)


read_and_reformate()
# liste = read()
#write_reformating()
liste.sort()
print (liste)
print (len(liste))
#create_children_files()
