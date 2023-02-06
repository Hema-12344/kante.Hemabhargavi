n=int(input("enter a number:"))
x=n
s=0
while x>=10:
    s=0
    while x>0:
        r=x%10
        s=s+r**2
        x=x//10
    x=s
if x==1:
    print("happy number")
else:
    print("not a happy number")
