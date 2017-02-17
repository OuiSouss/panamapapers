from neo4j.v1 import GraphDatabase, basic_auth


driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
session = driver.session()

result = session.run("MATCH (n) WHERE EXISTS(n.countries) RETURN DISTINCT \"node\" as element, n.countries AS countries")

countries = []
for r in result:
    c = r["countries"]
    c = c.split()
    for i in c:
        if i not in countries:
            countries.append(i)
    print (countries)
    print ("%s "%r["countries"])

session.close()

