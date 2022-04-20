def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n>0:

        if n==1:
            return  print(source + ' ' + dest)

        towerofhanoi(n-1,source , dest, aux)
        print(source + ' ' + dest)
        towerofhanoi(n-1,aux , source, dest)


        pass

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')