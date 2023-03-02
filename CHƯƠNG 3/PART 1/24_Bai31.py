a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
SLN=a
SBN=a
if SLN<b:
    SLN=b
elif SLN<c:
    SLN=c
print('SLN=',SLN,sep='')
if SBN>b:
    SBN=b
elif SBN>c:
    SBN=c
print('SBN=',SBN,sep="")

