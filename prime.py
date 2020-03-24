x=int(input("enter the number:"))
if x>1:
    for i in range(2,x//2):
     if(x%i)==0:
         print(x,"is not prime")
     else:
         print(x,"is prime")
else:
    print(x,"not prime")             