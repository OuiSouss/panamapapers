#!/bin/bash

./panamas/neo4j/bin/neo4j start

cd panamas/neo4j/import
../bin/neo4j-shell -file ../../../script_cypher_import.cypher
