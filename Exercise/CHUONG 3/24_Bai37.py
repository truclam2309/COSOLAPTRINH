n=int(input())
while n>=0:
    a=n
    j=1
    for i in range (1,n+1,1):
        if n>0:
            j=j*i
    print(j)
    print(a-1)
    n=n-1