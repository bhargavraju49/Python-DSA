import queue

class graph:
    def __init__(self,n):
        self.vertices = n
        self.adjMatrix = [[0 for i in range(n)] for j in range(n)]

    def addgraph(self,v1,v2):
        if self.adjMatrix[v1][v2] == 0:
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1
        else:
            return

    def bfs(self,v,e):
        if v==0:
            return
        if e == 0:
            for i in range(v):
                print(i,end=' ')
            return
        visited = [False for i in range(self.vertices)]
        for i1 in range(self.vertices):
            if visited[i1] is False:
                q = queue.Queue()
                q.put(i1)
                visited[i1] = True
                while q.qsize()>0:
                    o=q.get()
                    print(o,end=' ')
                    for i in range(self.vertices):
                        if visited[i] is False and self.adjMatrix[o][i]>0:
                            q.put(i)
                            visited[i] = True

    def haspath(self, v,e):
        visited = [False for i in range(self.vertices)]
        def helper_haspath (v,e):
            if self.vertices<=e:
                return False
            visited[v] = True
            if self.adjMatrix[v][e] or self.adjMatrix[e][v]  == 1:
                return True
            k = False
            for i in range(self.vertices):
                if self.adjMatrix[v][i]==1 and visited[i] is False:
                    k = helper_haspath(i,e)
                if k is True:
                    break
            if k is True:
                return True
            else:
                return False
        return helper_haspath(v,e)
    def __str__(self):
        return str(self.adjMatrix)

n = input().split(' ')

g = graph (int(n[0]))
for i in range(int(n[1])):
    k=input().split(' ')
    g.addgraph(int(k[0]),int(k[1]))

v = input().split(' ')
v1 = int(v[0])
e1 = int(v[1])

k = g.haspath(v1,e1)

if k is True:
    print('true')
else:
    print('false')