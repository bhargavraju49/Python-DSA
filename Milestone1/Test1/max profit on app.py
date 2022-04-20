def maximumProfit(a):
    a.sort()
    k= len(a)
    m = 0
    for i in range(k):
        tem = a[i]*(k-i)
        m = max(m,tem)
    return m

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)