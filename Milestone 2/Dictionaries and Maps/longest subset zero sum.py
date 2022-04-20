def subsetSum(l):
    k=dict()
    ma = 0
    sum = 0
    for i in range(len(l)):
        sum+=l[i]
        if sum ==0:
            ma = i+1
        else:
            if sum not in k:
                k[sum] = i
            else:
                ma = max(ma,i-k[sum])

    return ma


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))

#
# Sample Input 1:
# 10
#  95 -97 -387 -435 -5 -70 897 127 23 284
# Sample Output 1:
# 5
# Explanation:
# The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897