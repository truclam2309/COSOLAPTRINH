a=int(input('tien thu='))
VAT=float(0.1)
if (a>=1 and a<=100):
    T=a*550
elif (a>=101 and a<=150):
    T=100*550+(a-100)*750
elif (a>=151 and a<=200):
    T=100*550+50*750+(a-150)*950
else:
    T=100*550+50*750+50*950+(a-200)*1350
print('Phai tra=',T+T*VAT,sep='')