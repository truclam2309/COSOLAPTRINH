n=int(input('n='))
a=n+1
for i in range (1,a,1):
    if i%10==0:
        print(i)
    else:
        print(i,end=' ')