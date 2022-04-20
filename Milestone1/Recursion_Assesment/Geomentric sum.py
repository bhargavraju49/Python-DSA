## Read input as specified in the question.
## Print output as specified in the question.
def gp (n ,k):
    if n == 0:
        return 0
    if n > 0:
        return k + gp(n - 1 ,k / 2)


n = int(input())
print(format(gp(n + 1 ,1) ,'.5f'))