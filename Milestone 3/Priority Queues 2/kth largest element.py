import heapq
def kthLargest(lst, k):
    a = lst[:k]
    heapq.heapify(a)
    for i in range(k,len(lst)):
        if a[0]<lst[i]:
            heapq.heapreplace(a,lst[i])
    # heapq._heapify_max(a)
    return a[0]


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)