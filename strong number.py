n=int(input("enter a number:"))
temp=n
s=0
while n:
    i=1
    fact=1
    r=n%10
    while i<=r:
        fact=fact*i
        i=i+1
    s=s+fact
    n=n//10
if s==temp:
    print(temp ,"strong number")
else:
    print(temp,"is not a strong number")
        
