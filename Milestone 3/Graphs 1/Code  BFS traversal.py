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
        pass
    def __str__(self):
        return str(self.adjMatrix)

n = input().split(' ')

g = graph (int(n[0]))
for i in range(int(n[1])):
    k=input().split(' ')
    g.addgraph(int(k[0]),int(k[1]))
g.bfs(int(n[0]),int(n[1]))