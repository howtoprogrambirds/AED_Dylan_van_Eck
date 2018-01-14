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


def is_connected(G):
    s = vertices(G)[0]
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = math.inf  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == math.inf: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)
    connected = True
    for i in V:
        if i.distance == math.inf:
            connected = False
            break
    return connected


def flip_arrow(G):
    newG = dict()
    for i in G:
        for x in G[i]:
            if x not in newG:
                newG[x] = []
            newG[x].append(i)
    return newG

def is_strongly_connected(G):
    return is_connected(G) and is_connected(flip_arrow(G))


if __name__ == '__main__':
    v = [Vertex(i) for i in range(8)]
    G1 = {
        v[0]: [v[1]],
        v[1]: [v[2]],
        v[2]: [v[0]]
    }
    G2 = {
        v[0]: [v[1]],
        v[2]: [v[0], v[1]]
    }

    print(is_strongly_connected(G1))
    print(is_strongly_connected(G2))