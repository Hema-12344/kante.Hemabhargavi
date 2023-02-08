s=input("enter a character:")
ns=''
rs=''
r=''
for i in range(0,len(s),2):
    rs=s[i]
    i=i+1
    ns=int(s[i])
    r=r+rs*ns
print(r)
    
        
       
