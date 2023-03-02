n=int(input('n='))
b=1
if n==0:
    print(str(n)+'!='+str(1))
elif n>0 and n<=100:
    for i in range (1,n+1,1):
        b=b*i
    print(str(n)+'!=',b,sep='')
