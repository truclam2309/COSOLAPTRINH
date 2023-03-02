i=0
j=0
while True:
    n=int(input())
    if n>0:
        i=i+1
    elif n<0:
        j=j+1
    elif n==0:
        break
print(str(i)+' so duong')
print(str(j)+' so am')