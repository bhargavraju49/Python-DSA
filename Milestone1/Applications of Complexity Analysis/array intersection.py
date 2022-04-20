from sys import stdin


def intersection(arr1, arr2, n, m):
    arr1.sort()
    arr2.sort()
    c=[]
    if n<m:
        return intersection(arr2, arr1, m, n)
    i=0
    j=0
    while(j<m and i<n):
        if arr1[i]>arr2[j]:
            j=j+1
        elif arr1[i]==arr2[j]:
            c.append(arr1[i])
            i=i+1
            j=j+1

        elif arr1[i]<arr2[j]:
            i=i+1
    return c




# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()
    k = intersection(arr1, arr2, n, m)
    print(*k)

    t -= 1
