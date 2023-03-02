while True: 
    a=float(input('a='))
    b=float(input('b='))
    c=str(input('Toan tu:'))
    if c=='+':
        print(str(a)+str(c)+str(b)+'=',a+b,sep='')
    elif c=='-':
        print(str(a)+str(c)+str(b)+'=',a-b,sep='')
    elif c=='*':
        print(str(a)+str(c)+str(b)+'=',a*b,sep='')
    elif c=='/':
        print(str(a)+str(c)+str(b)+'=',a/b,sep='')
    d=str(input('Tiep tuc:'))
    if d=='T' or d=='t':
        break