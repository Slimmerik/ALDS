class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data

import math
import copy

INFINITY = math.inf  # float("inf")

def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]

v = [Vertex(i) for i in range(9)]
Voorbeeld = {v[0]: [v[4], v[5]],
                  v[1]: [v[4], v[5], v[6]],
                  v[2]: [v[4], v[5], v[6]],
                  v[3]: [v[7]],
                  v[4]: [v[0],v[2], v[1], v[5]],
                  v[5]: [v[4], v[0], v[1], v[2]],
                  v[6]: [v[1], v[2]],
                  v[7]: [v[3]],
                  v[8]: []
                  }
bridgevoorbeeld = {v[0]: [v[1], v[3]],
                  v[1]: [v[0], v[2]],
                  v[2]: [v[1], v[3], v[4]],
                  v[3]: [v[0], v[2]],
                  v[4]: [v[2], v[5], v[6]],
                  v[5]: [v[4], v[6]],
                  v[6]: [v[4], v[5], v[7]],
                  v[7]: [v[6]],
                  v[8]: []
                  }

notStrongly = {v[0]: [v[1]],
                  v[1]: [],
                  v[2]: [v[1],v[0]],
                  v[3]: [],
                  v[4]: [],
                  v[5]: [],
                  v[6]: [],
                  v[7]: [],
                  v[8]: []
                  }

strongly = {v[0]: [v[1]],
                  v[1]: [v[2]],
                  v[2]: [v[0]],
                  v[3]: [],
                  v[4]: [],
                  v[5]: [],
                  v[6]: [],
                  v[7]: [],
                  v[8]: []
                  }

euler_circuit = {v[0]: [v[1], v[2]],
                  v[1]: [v[0], v[3]],
                  v[2]: [v[0], v[3]],
                  v[3]: [v[1], v[2], v[4], v[6]],
                  v[4]: [v[3], v[5], v[6], v[7]],
                  v[5]: [v[4], v[6]],
                  v[6]: [v[3], v[4], v[5], v[7]],
                  v[7]: [v[4], v[6]],
                  v[8]: []
                  }

def is_connected(g, first, last):
    if last in build_predecessors(g, first).keys():
        return True
    else:
        return False


def build_predecessors(g, first):
    prelist = {}
    que = []
    queisNone = False
    current = first
    prelist[first] = None
    while not queisNone:
        for temp in g[current]:
            if temp not in prelist.keys():
                que.append(temp)
                prelist[temp] = current
        if len(que) == 0:
            queisNone = True
        if len(que) != 0:
            current = que.pop(0)
    return prelist

def is_Euler_graph(g):
    re = True
    last = None
    for key in g.keys():
        for value in g[key]:
            if last == None:
                last = len(g[value])
            if len(g[value]) != last:
                re = False
    return re

print(is_Euler_graph(notStrongly))
print(is_Euler_graph(strongly))

def get_Euler_circuit(g,s):
    startNodeVec = s
    circList = [s]
    currentKey = s
    workingGraph = {}
    for key in g.keys():
        workingGraph[key] = g[key][:]
    notDone = True
    while notDone:
        for value in workingGraph[currentKey]:
            workingGraph[currentKey].remove(value)
            workingGraph[value].remove(currentKey)
            createsBridge = False
            for t in workingGraph.keys():
                for v in workingGraph[t]:
                    if not is_connected(workingGraph,value, v):
                        createsBridge = True
            if  not createsBridge:
                circList.append(value)
                currentKey = value
                continue
            else:
                workingGraph[currentKey].append(value)
                workingGraph[value].append(currentKey)
        if startNodeVec == currentKey:
            notDone = False
    return circList






print(get_Euler_circuit(euler_circuit, v[0]))
