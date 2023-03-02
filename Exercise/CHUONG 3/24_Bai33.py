x=float(input("x="))
y=float(input('y='))
ch=str(input('Phep toan:'))
if ch=='+' or ch=='-' or ch=='*' or ch=='/':
    if ch=='+':
        T=x+y
        print(str(x)+str(ch)+str(y)+'=',T,sep='')
    elif ch=='-':
        T=x-y
        print(str(x)+str(ch)+str(y)+'=',T,sep='')
    elif ch=='*':
        T=x*y
        print(str(x)+str(ch)+str(y)+'=',T,sep='')
    elif ch=='/':
        if y==0:
           print('Khong hop le')
        else:
            T=x/y
            print(str(x)+str(ch)+str(y)+'=',T,sep='') 
else:
    print('Khong hop le')

    
    
        
    