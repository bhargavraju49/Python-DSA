def maxFreq (l):
    d = dict()
    for i in l:
        d[i] = d.get(i ,0) + 1

    max = -1
    for x in l:
        if d[x] > max:
            max = d[x]
            num = x

    return num


n = int(input())
l = list(int(i) for i in input().strip().split(' ')[:n])
print(maxFreq(l))