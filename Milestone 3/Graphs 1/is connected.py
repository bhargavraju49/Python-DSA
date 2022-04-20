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
        if v==0 or v==1:
            return True
        if e == 0:
            return False
        visited = [False for i in range(self.vertices)]
        i1 = 0
        if visited[i1] is False:
            q = queue.Queue()
            q.put(i1)
            visited[i1] = True
            while q.qsize()>0:
                o=q.get()
                for i in range(self.vertices):
                    if visited[i] is False and self.adjMatrix[o][i]>0:
                        q.put(i)
                        visited[i] = True
        for i in visited:
            if i is False:
                return False
        return True

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

    def getpath(self,v,e):

        visited = [False for i in range(self.vertices)]

        def helper_getpath (sv,ev):
            if sv == ev:
                return list([sv])

            visited[sv] = True

            for i in range(self.vertices):
                if self.adjMatrix[sv][i] == 1 and not visited[i]:
                    li = helper_getpath(i ,ev)

                    if li != None:
                        li.append(sv)
                        return li

            return None
        return helper_getpath(v,e)

    def __str__(self):
        return str(self.adjMatrix)

n = input().split(' ')

g = graph (int(n[0]))
for i in range(int(n[1])):
    k=input().split(' ')
    g.addgraph(int(k[0]),int(k[1]))
k = g.bfs(int(n[0]),int(n[1]))
if k is True:
    print('true')
else:
    print('false')