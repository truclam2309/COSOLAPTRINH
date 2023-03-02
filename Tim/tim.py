n=int(input())
for i in range (1,n+1,1):
    for j in range (1,n-i+1,1):
        print(' ',end=' ')
    for k in range (1,(2*i)+2,1):
        print('*',end=' ')
    for j in range (1,n-i+1,1):
        print('  ',end='  ')
    for k in range (1,(2*i)+2,1):
        print('*',end=' ')
    print()
for a in range (1,n,1):
    print('* '*(4*n+2))
for m in range (1,n*2+2,1):
    for b in range (1,m+1,1):
        print(' ',end=' ')
    for c in range (n*4+1,2*m-1,-1):
        print('*',end=' ')
    print()
    