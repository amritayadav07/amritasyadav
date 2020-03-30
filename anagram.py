from collections import Counter
x = 'ant magenta magnate tan gmanate'
x = x.split(' ')
for i in range(len(x)):
   x[i]=''.join(sorted(x[i]))
   dic = Counter(x)
print(max(dic.values()))           