n=int(input('n='))
a=2
for i in range (2,9,1):
    if n%i==0:
        print(str(n)+' khong la SNT')
        break
else:
    print(str(n)+' la SNT')
    
