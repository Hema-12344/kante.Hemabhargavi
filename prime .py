a=1
fc=0
n=int(input("enter a number:"))
while a<=n:
    if n%a==0:
         fc=fc+1
    a=a+1              
if fc==2:
    print("prime number")
else:
    print("not a prime number")
