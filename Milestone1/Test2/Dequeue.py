class QueueUsingArray:
    def __init__(self):
        self.__arr=[]
        self.__count=0
    def insertRear (self,data):
        if self.__count==10:
            return -1
        self.__arr.append(data)
        self.__count+=1
        return self.__arr
    def insertFront (self,data):
        if self.__count==10:
            return -1
        self.__arr=[data]+self.__arr
        self.__count+=1
        return self.__arr
    def deleteRear (self):
        if self.__count==0:
            print (-1)
        else:
            self.__arr.pop(-1)
            self.__count -= 1
            return self.__arr
    def deleteFront (self):
        if self.__count == 0:
            print(-1)
        else:
            self.__arr.pop(0)
            self.__count -= 1
            return self.__arr
    def getFront (self):
        if self.__count == 0:
            return -1
        return self.__arr[0]
    def getRear (self):
        if self.__count == 0:
            return -1
        return self.__arr[-1]

t = [int(x) for x in input().split(" ")]
i = 0
A = QueueUsingArray()
while t[i]!=-1:
    n = t[i]
    i += 1
    if n == 1:
        k = A.insertFront (t[i])
        if k == -1:
            print (k)
        i += 1
    elif n == 2:
        k = A.insertRear (t[i])
        if k == -1:
            print (k)
        i += 1
    elif n == 3:
        A.deleteFront ()
    elif n == 4:
        A.deleteRear()
    elif n == 5:
        print(A.getFront())
    elif n == 6:
        print(A.getRear())

