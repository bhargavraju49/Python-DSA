def split(a):
    co = 0
    for i in a:
        if i % 5 == 0:
            co = co + 1
    a.sort()
    k = sum(a)
    if k % 2 == 1:
        return False
    s = k // 2
    chk = False
    c = 0
    i = 0
    visited = []
    while (i < len(a)):
        if i > 0:
            visited.append(a[i - 1])
        if c == s:
            chk = True
            break
        elif c < s:
            c = c + a[i]
            i = i + 1
        else:
            if c - s in visited:
                visited.remove(c - s)
                chk = True
                break
            else:
                c = c - visited[0]
                visited = visited[1:]
    if chk is False:
        return chk
    else:
        f = 0
        for i in visited:
            if i%5==0:
                f=f+1
        if f==0 or f==co:
            return False
        else:
            return True



n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr)
if ans is True:
    print('true')
else:
    print('false')