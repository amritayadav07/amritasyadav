x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
if x>y:
  r=y
else:
    r=x
    for i in range(1,r+1):
     if x%i==y%i==0:
      print(i)