temp=int(input("enter a temp:"))
if temp>=40:
    print("this is very hot")
elif temp>30 and 40:
    print("then its hot")
elif temp>20 and 30:
    print("then normal in temp")
elif temp>10 and 20:
    print("cold weather")
elif temp>0 and 10:
    print("very cold weather")
else:
    print("then freezing weather")
