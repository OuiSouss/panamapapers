match (n:Global)-[r]->(m:Global) where not(n:Address) AND not (m:Address) return n,r,m limit 30
match (n:Global)-[r]->(m:Global) where n.sourceID="Panama Papers" and not (n:Address and m:Address) and exists(startNode(r).countries) and exists(endNode(r).countries) return n.sourceID

match (n:Global)-[r]->(m:Global) where n.sourceID="Panama Papers" and exists(startNode(r).countries) and exists(endNode(r).countries) and (n.countries <> m.countries) and not (n:Address and m:Address) return distinct split(n.countries, ";") as country_list1
union
match (n:Global)-[r]->(m:Global) where n.sourceID="Panama Papers" and exists(startNode(r).countries) and exists(endNode(r).countries) and (n.countries <> m.countries) and not (n:Address and m:Address) return distinct split(m.countries, ";") as country_list2


///////:§dfdkljwhfzeui

match (n:Global)-[r]->(m:Global) where n.sourceID="Panama Papers" and exists(startNode(r).countries) and exists(endNode(r).countries) and (n.countries <> m.countries) and not (n:Address and m:Address) with distinct [split(n.countries,";"), split(m.countries,";")] as list unwind list as c unwind c as country return distinct country
