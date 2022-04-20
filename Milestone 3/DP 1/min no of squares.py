import sys ,math


def minSquaresI (n):
    dp = [-1 for i in range(n + 1)]
    dp[0] = 0

    for i in range(1 ,n + 1):
        ans = sys.maxsize
        root = int(math.sqrt(i))
        for j in range(1 ,root + 1):
            currAns = 1 + dp[i - (j ** 2)]
            ans = min(ans ,currAns)
        dp[i] = ans
    return dp[n]


n = int(input())
ans = minSquaresI(n)
print(ans)

# Sample Test Cases:
# Sample Input 1:
# 100
# Sample Output 1:
# 1
# Explanation:
# We can write 100 as 10^2 also, 100 can be written as (5^2) + (5^2) + (5^2) + (5^2), but this representation
# requires 4 squares. So, in this case, the expected answer would be 1, that is, 10^2.