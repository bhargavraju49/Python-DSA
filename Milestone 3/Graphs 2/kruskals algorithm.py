class Edge:
    def __init__ (self ,src ,dst ,wt):
        self.src = src
        self.dst = dst
        self.wt = wt


def getparent (v ,parent):
    if v == parent[v]:
        return v
    return getparent(parent[v] ,parent)


def kruskals (edges ,n ,e):
    edges = sorted(edges ,key=lambda edge: edge.wt)
    output = []

    parent = [i for i in range(n)]

    count = 0
    i = 0
    while count < n - 1:
        currEdge = edges[i]
        v1P = getparent(currEdge.src ,parent)
        v2P = getparent(currEdge.dst ,parent)

        if v1P != v2P:
            output.append(currEdge)
            count += 1
            parent[v1P] = v2P
        i += 1

    return output


ip = [int(ele) for ele in input().split()]
v = ip[0]
e = ip[1]
edges = []

for i in range(e):
    ipe = [int(ele) for ele in input().split()]
    edge = Edge(ipe[0] ,ipe[1] ,ipe[2])
    edges.append(edge)

output = kruskals(edges ,v ,e)

for ele in output:
    if (ele.src < ele.dst):
        print(str(ele.src) + " " + str(ele.dst) + " " + str(ele.wt))
    else:
        print(str(ele.dst) + " " + str(ele.src) + " " + str(ele.wt))
