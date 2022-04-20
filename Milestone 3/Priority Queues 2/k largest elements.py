import heapq
def kLargest(lst, k):
    a = lst[:k]
    heapq.heapify(a)
    for i in range(k,len(lst)):
        if a[0]<lst[i]:
            heapq.heapreplace(a,lst[i])
    return a

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')
