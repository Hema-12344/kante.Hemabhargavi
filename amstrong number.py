n=int(input("enter a number:"))
t=n
s=0
d=0
while n>0:
    d=d+1
    n=n//10
n=t
while n>0:
    r=n%10
    s=s+r**d
    n=n//10
if s==t:
    print("armstrong number")
else:
     print(" not a armstrong  number")
