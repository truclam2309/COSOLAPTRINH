n=int(input('n='))
a=1
while n>=1 and n<=50 and a<=n:
    if (a%10)!=0:
        print(a,end=' ')
    else:
        print(a)
    a=a+1