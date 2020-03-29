a = []
n = int(input("enter the no:"))
for x in range(n):
    print(x+1,"enter list")
    a.append(input())
N = 'rep'    
has = set()
for x in range(len(a)):
    if a[x] in has:
      a[x] = N
    has.add(a[x]) 
print(a)        