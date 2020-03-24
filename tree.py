x=int(input("enter the no:"))
for i in range(0,x):
    for j in range(0,x-i-1):
        print(end=" ")
    for j in range(0,i+1):
         print("*",end=" ")
    print()