class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data

import math

INFINITY = math.inf  # float("inf")

def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]

v = [Vertex(i) for i in range(9)]
VoorbeeldEdges = {v[0]: [v[4], v[5]],
                  v[1]: [v[4], v[5], v[6]],
                  v[2]: [v[4], v[5], v[6]],
                  v[3]: [v[7]],
                  v[4]: [v[0], v[1], v[5]],
                  v[5]: [v[4], v[0], v[1], v[2]],
                  v[6]: [v[1], v[2]],
                  v[7]: [v[3]],
                  v[8]: []
                  }
cyclevoorbeeld = {v[0]: [v[4], v[5]],
                  v[1]: [v[4], v[6]],
                  v[2]: [v[5]],
                  v[3]: [v[7]],
                  v[4]: [v[0], v[1]],
                  v[5]: [v[0], v[2]],
                  v[6]: [v[1]],
                  v[7]: [v[3]],
                  v[8]: []
                  }


def no_cycles(g,first):
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
            elif temp in prelist.keys() and current not in g[temp]:
                return False
        if len(que) == 0:
            queisNone = True
        if len(que) != 0:
            current = que.pop(0)
    return True

print( no_cycles(cyclevoorbeeld, v[5]) )

print( no_cycles(VoorbeeldEdges, v[5]) )