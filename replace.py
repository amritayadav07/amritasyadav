a=[]
n = int(input("enter the no:"))
for x in range(n):
    print(x+1,"enter list")
    a.append(input())
s = set(a)
a = list(s)
for x in a: 
 print(x)        