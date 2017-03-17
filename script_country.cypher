//creation de pays et relation
//on cherche deux sommets dans global quih ne sont pas des addresses
// et qui sont des panama papers, qui existent et sont de pays différents

// on met dans une liste les sommets pays splités

// afin de ne travailler que sur un sommet à la fois, on unwind les listes dans deux nouvelles variables.

// a partir de ses variables, on réalise des merges, ce qui nous permet de ne pas avoir d'intéractions dupliquées.

// à la création de l'arête, on crée un label interaction équipé d'un compteur qui compte le nombre d'interactions totales entre deux pays.

// ce compteur est mis à jour grace à la fonction set


match ()-[r]->() where startNode(r) <> endNode(r) and startNode(r):Global and endNode(r):Global and startNode(r).sourceID="Panama Papers" and exists(startNode(r).countries) and exists(endNode(r).countries) and (startNode(r).countries <> endNode(r).countries) and not (startNode(r):Address and endNode(r):Address) with split(startNode(r).countries,";") as node1, split(endNode(r).countries, ";") as node2 
unwind node1 as nodeD
unwind node2 as nodeE
merge (n1:Country {country: node1})
merge (n2:Country {country: node2})
merge (ns:Country {country: nodeD})-[i:interaction {cpt_int: 0}]->(ne:Country {country: nodeE}) 
set i.cpt_int = toInteger(i.cpt_int)+1