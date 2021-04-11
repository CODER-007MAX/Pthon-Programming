s = input()
l = s.split()
m = []
for i in l:
    if (s.count(i)>1 and (i not in m) or s.count(i) == 1):
       m.append(i)
print(' '.join(m))
