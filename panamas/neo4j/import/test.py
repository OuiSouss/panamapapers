from neo4j.v1 import GraphDatabase, basic_auth

import os
import json

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def kparmisn(k,n):
    return fact(n)/(fact(k)*fact(n-k))

driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
session = driver.session()

outfile = open ('data.json','w')

countries_array = ['South Africa', 'Liechtenstein', 'Monaco', 'Belgium', 'Lebanon', 'Switzerland', 'Malaysia', 'Spain', 'United Kingdom', 'Jersey', 'France', 'Luxembourg', 'Taiwan', 'Estonia', 'Mexico', 'Argentina', 'Guernsey', 'United States', 'Venezuela', 'Hong Kong', 'Panama', 'Saudi Arabia', 'Germany', 'Kuwait', 'Poland', 'Brazil', 'Turkey', 'Egypt', 'Canada', 'Portugal', 'Russia', 'Isle of Man', 'Malta', 'Hungary', 'Israel', 'Greece', 'Philippines', 'Italy', 'China', 'Gibraltar', 'Bahamas', 'Honduras', 'Australia', 'Austria', 'Sweden', 'Slovenia', 'Uruguay', 'Thailand', 'Ecuador', 'Colombia', 'United Arab Emirates', 'Peru', 'Czech Republic']

number_of_countries = len(countries_array)
data = {}
data['nodes'] = [{}] * number_of_countries
data['links'] = [{}] * kparmisn(2,number_of_countries)

x = 0

for i,country1 in enumerate(countries_array):
    data['nodes'][i] = {'id': country1}
    for j in range(i+1,number_of_countries):
        s = 0
        country2 = countries_array[j]
        exist = False
        result = session.run("MATCH (n:Country)-[r]->(m:Country) WHERE (n.country = '" + country1 + "' and m.country = '" + country2 + "') or (n.country = '" + country2 + "' and m.country = '" + country1 + "') RETURN r.cpt_interaction as inter")
        for r in result:
            exist = True
            s += r["inter"]
        data['links'][x] = {'source': country1, 'target': country2, 'value': s}
        x += 1
    print(i)

json.dump(data, outfile)

outfile.close
session.close()
