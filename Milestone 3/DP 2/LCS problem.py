from sys import stdin


def lcs(s, t):
    m=len(s)
    n=len(t)
    dp=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if s[i]==t[j]:
                dp[i][j] = dp[i+1][j+1]+1
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
    return dp[0][0]
pass


# main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))