from sys import stdin


def knapsack(wt, val, W):
    n = len(val)
    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if j < wt[i - 1]:
                ans = dp[i - 1][j]
            else:
                ans1 = val[i - 1] + dp[i - 1][j - wt[i - 1]]
                ans2 = dp[i - 1][j]
                ans = max(ans1, ans2)
            dp[i][j] = ans
    return dp[n][W]



def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight


#main
weights, values, n, maxWeight = takeInput()

print(knapsack(weights, values, maxWeight))