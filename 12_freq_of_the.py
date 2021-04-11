s = input()
n = s.split()
k = 'the'
t = 0
for i in range (0, len(n)):
    if (k==n[i]):
        t += 1
print(t)
