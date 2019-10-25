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

def is_strongly_connected(g):
    toBeChecked = list(g.keys())[0]
    pred = build_predecessors(g,toBeChecked)
    strongly = True
    for t in g.keys():
        if len(g[t]) > 0:
            if t not in pred:
                strongly = False
    q = {}
    for t in g.keys():
        q[t] = []

    for key in g.keys():
        for value in g[key]:
            if value not in q.keys():
                q[value] = []
            q[value].append(key)

    predrev = build_predecessors(q, toBeChecked)

    for t in g.keys():
        if len(g[t]) > 0:
            if t not in predrev:
                strongly = False

    return strongly

print(is_strongly_connected(notStrongly))
print(is_strongly_connected(strongly))
