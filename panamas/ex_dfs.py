#!/usr/bin/env python
#-*- coding: utf-8 -*-s

from neo4j.v1 import GraphDatabase, basic_auth


driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "neo"))
session = driver.session()

#Voilà comme je serais pas là demain
#ceci est ce que je te propose

#une liste qui faut gérer comme une pile
#tu append et remove

#je te donne un exemple à adapter

"""
def reverseFileLoader():

    graph = collections.defaultdict(lambda: {'g': [], 's': False, 't': None, 'u': None })
    for line in open('/home/edd91/Documents/SCC.txt'):
        k, v = map(int, line.split())
        graph[v]['g'].append(k)

    return graph

def DFS(graph, i):
    global t
    global source
    stack = []
    seen = []
    seen.append(i)
    stack.append(i)

    while stack:
        s = stack[-1]
        j = len(graph[s]['g']) - 1
        h = 0
        while (j >= 0):
            if graph[s]['g'][j] not in seen and graph[graph[s]['g'][j]]['t'] == None:
                seen.append(graph[s]['g'][j])
                stack.append(graph[s]['g'][j])
                h += 1
            j -= 1

        if h == 0:
            if graph[s]['t'] == None:
                t += 1
                graph[s]['u'] = source
                graph[s]['t'] = t 
            stack.pop()

def DFSLoop(graph):
    global t
    t = 0
    global source
    source = None
    i = len(graph)
    while (i >= 1):
        print "running for " + str(i)
        source = i
        DFS(graph, i)
        i -= 1
"""
result = session.run("MATCH (n:Global) return n as node_racine")
