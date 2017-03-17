//creation de pays et relation
//on cherche deux sommets dans global quih ne sont pas des addresses
// et qui sont des panama papers, qui existent et sont de pays différents

// on met dans une liste les sommets pays splités

// afin de ne travailler que sur un sommet à la fois, on unwind les listes dans deux nouvelles variables.

// a partir de ses variables, on réalise des merges, ce qui nous permet de ne pas avoir d'intéractions dupliquées.

// à la création de l'arête, on crée un label interaction équipé d'un compteur qui compte le nombre d'interactions totales entre deux pays.

// ce compteur est mis à jour grace à la fonction set


match (n:Global {sourceID:"Panama Papers"})-[r]->(m:Global) where exists(n.countries) and exists(m.countries) and not (n:Address and m:Address) with split(n.countries,";") as node1, split(m.countries, ";") as node2 
unwind node1 as nodeD
unwind node2 as nodeE
merge (n1:Country3 {country: nodeD})
merge (n2:Country3 {country: nodeE})
merge (n1)-[i:interaction {cpt_int: 0}]->(n2) 
set i.cpt_int = toInt(i.cpt_int)+1

match (n:Country) -[r]->(n:Country) delete r


/*

match (n:Global {sourceID:"Panama Papers"})-[r]->(m:Global) where exists(n.countries) and exists(m.countries) and not(n:Address or m:Address) with split(n.countries,";") as node1, split(m.countries, ";") as node2 
unwind node1 as nodeD
unwind node2 as nodeE
merge (n1:Country3 {country: nodeD})
with n1, nodeD, nodeE, node1, node2
optional match (n2:Country3 {country: nodeE}) where nodeD<>nodeE
set n2.country = nodeE
merge (n:Country {country: nodeE})
merge (n1)-[i:interaction {cpt_int: 0}]->(n2) 
set i.cpt_int = toInt(i.cpt_int)+1
*/
