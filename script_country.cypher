//creation de pays et relation
//on cherche deux sommets dans global quih ne sont pas des addresses
// et qui sont des panama papers, qui existent et sont de pays différents

// on met dans une liste les sommets pays splités

//on crée les sommets une seule et unique fois dans un merge durant un foreach



match (n:Global)-[r]->(m:Global) where n.sourceID="Panama Papers" and exists(startNode(r).countries) and exists(endNode(r).countries) and (n.countries <> m.countries) and not (n:Address and m:Address) with split(n.countries,";") as node1, split(m.countries, ";") as node2 
foreach (node in node1 | merge (:Country2 {country: node}))
foreach (node in node2 | merge (:Country2 {country: node}))
