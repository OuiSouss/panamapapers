#!/usr/bin/env python
#-*- coding: utf-8 -*-s

from neo4j.v1 import GraphDatabase, basic_auth
#import os

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
session = driver.session()

result = session.run("MATCH (n) WHERE EXISTS(n.countries) RETURN DISTINCT \"node\" as element, n.countries AS countries")

l_countries = []
for r in result:
    i = r["countries"]
    i = i.encode("utf-8")
    c = i.split(";")
    for s in c :
        if s not in l_countries:
            l_countries.append(s)

print (len(l_countries))
#print (l_countries[106])
#print (l_countries[107])
#print (l_countries[108])


#os.system("{ echo \"export pays='France'\" ; cat; } | neo4j/bin/neo4j-shell")

for n in l_countries:
    n = n.decode('utf-8')
    n = n.replace("'", " ")
    c = "'%s'"%n
    print (c)
    session.run("create (c:Country{country:%s})"%c)

    
session.close()

