from sys import stdin

MAX_VALUE = 2147483647


def minCostPath(a, n, m):
    dp=[[MAX_VALUE for i in range (m+1) ]for i in range(n+1)]

    for i in range (n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i==n-1 and j==m-1:
                dp[i][j] = a[i][j]
            else:
                a1 = dp[i][j+1]
                a2 = dp[i+1][j]
                a3 = dp[i+1][j+1]
                ans = min(a1,a2,a3)+a[i][j]
                dp[i][j]=ans

    return dp[0][0]

# Your code goes here


# taking input using fast I/O method
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])

    if mRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


# main
mat, mRows, nCols = take2DInput()
print(minCostPath(mat, mRows, nCols))