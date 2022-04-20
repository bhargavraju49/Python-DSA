from sys import stdin


def longestConsecutiveSubsequence(a, n):
    k = dict.fromkeys(a,1)
    max = 0
    for i in k:
        j=i+1
        s=1
        while(k.get(j)):
            s += 1
            j+=1
        if s>=max:
            max = s
            k[i] = s
    for i in a:
        if k[i]==max:
            return [i,i+max-1]
    pass


def takeInput():
    # To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


# Main
arr, n = takeInput()
ans = longestConsecutiveSubsequence(arr, n)
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)