class PriorityQueueNode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele

    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2

            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self, ele, priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        i = 0

        while 2 * i + 1 <= self.getSize() - 1:
            h = self.pq[i].priority
            x = self.pq[2 * i + 1].priority
            if 2 * i + 2 < self.getSize() - 1:
                y = self.pq[2 * i + 2].priority
                k = max(x, y)
            else:
                k = x
            if k == x:
                v = 2 * i + 1
            else:
                v = 2 * i + 2
            if h < k:
                self.pq[i], self.pq[v] = self.pq[v], self.pq[i]
                i = v
            else:
                break

    def removeMax(self):
        if self.isEmpty():
            return None

        k = self.pq[0].ele
        self.pq[0] = self.pq.pop()
        self.__percolateDown()
        return k


myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        myPq.insert(element, element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i += 1