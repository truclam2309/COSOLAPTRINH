a=input('Ho ten: ')
b=int(input('So ngay cong: '))
c=int(input('Don gia ngay cong: '))
d=float(input('He so phu cap: '))
e=int(input('Tam ung: '))
L=c*b*d
T=L-e
print('Nhan vien',a,end=", ")
print('Co tien Luong=',round(L,1),sep='',end=", ")
print('Tam ung=',e,sep='',end=" va ")
print('Thuc linh=',round(T,1),sep='')