import math


class myqueue(list):
    def __init__(self,a=list()):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)

class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]


def is_connected(G, v1, v2):
    V = vertices(G)
    v1.predecessor = None
    v1.distance = 0
    for v in V:
        if v != v1:
            v.distance = math.inf  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(v1)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == math.inf: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)
    return v2.distance != math.inf


def get_bridges(G):
    bridges = list()
    for v in G:
        for c in G[v]:
            index = G[v].index(c)
            del G[v][index]
            if not is_connected(G, v, c):
                bridges.append((v, c))
            G[v].insert(index, c)
    return bridges


def is_Euler_graph(G):
    for i in G:
        if len(G[i])%2 == 1:
            return False
    return True


def getEuler_circuit(G, s):
    path = list()
    if not is_Euler_graph(G):
        return path
    path.append(s)
    while s != None:
        if len(G[s]) == 0:
            break
        bridges = get_bridges(G)
        for i in range(len(G[s]) - 1):
            if (G[s][i], s) not in bridges:
                t = G[s][i]
                break
        if t == s:
            t = G[s][-1]
        del G[s][G[s].index(t)]
        del G[t][G[t].index(s)]
        path.append(t)
        s = t
    return path


def main():
    v = [Vertex(i) for i in range(8)]

    G = {
        v[0]: [v[1], v[2]],
        v[1]: [v[0], v[3]],
        v[2]: [v[0], v[3]],
        v[3]: [v[1], v[2], v[4], v[6]],
        v[4]: [v[3], v[5], v[6], v[7]],
        v[5]: [v[4], v[6]],
        v[6]: [v[3], v[4], v[5], v[7]],
        v[7]: [v[4], v[6]]
    }

    print(is_Euler_graph(G))
    print(getEuler_circuit(G, v[0]))


if __name__ == '__main__':
    main()