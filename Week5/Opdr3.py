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

def get_bridges(g):

    brdigelist = []
    q = copy.copy(g)

    for key in g.keys():
        for value in g[key]:
            print(g)
            print(key, value)
            keydel = g[key][:]
            keydel.remove(value)
            q[key] = keydel

            valdel = g[value][:]
            valdel.remove(key)
            q[value] = valdel

            if not is_connected(q,key,value):
                brdigelist.append([key,value])
            print(q)

            print("")
            q[key]= g[key]
            q[value] = g[value]
    return brdigelist

# print(is_connected(bridgevoorbeeld, v[0],v[7]))

print(get_bridges(bridgevoorbeeld))
print(get_bridges(Voorbeeld))