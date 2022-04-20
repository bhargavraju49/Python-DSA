def merge(a1, a2, arr):
    i = 0
    j = 0
    st = 0
    while i < len(a1) and j < len(a2):
        if a1[i] > a2[j]:
            arr[st] = a2[j]
            j = j + 1
            st = st + 1
        else:
            arr[st] = a1[i]
            i = i + 1
            st = st + 1
    while i<len(a1):
        arr[st] = a1[i]
        st=st+1
        i=i+1
    while j<len(a2):
        arr[st] = a2[j]
        st=st+1
        j=j+1


def mergeSort(arr, start, end):
    if end == 0 or end == 1:
        return
    mid = end // 2


    a1 = arr[:mid]
    a2 = arr[mid:]

    mergeSort(a1, 0, len(a1))
    mergeSort(a2, 0, len(a2))

    merge(a1, a2, arr)

    pass

# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)
