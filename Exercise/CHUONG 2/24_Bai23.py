import math
print('Nhap hai canh ke cua tam giac vuong:')
a=int(input())
b=int(input())
x=math.sqrt(a**2+b**2)
print('Canh ke thu nhat:',a,end=", ")
print('canh ke thu hai:',b,end=", ")
print('co canh huyen =',round(x,2))