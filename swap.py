x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
print("before swapping:")
print("value of x:",x,"and y:",y)
x+=y
y=x-y
x=x-y
print("after swapping")
print("value of x:",x,"and y:",y)