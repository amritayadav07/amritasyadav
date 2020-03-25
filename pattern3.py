n=int(input("enter the no:"))
for row in range(1,n+1):
    if row%3==0:
        print("*"*5)
    else:
        print("*"," ","*")    