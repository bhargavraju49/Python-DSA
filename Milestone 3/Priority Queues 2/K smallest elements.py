import heapq
def kSmallest(lst, k):
    a = lst[:k]
    heapq._heapify_max(a)
    for i in range(k,len(lst)):
        if a[0]>lst[i]:
            heapq._heapreplace_max(a,lst[i])
    return a

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')