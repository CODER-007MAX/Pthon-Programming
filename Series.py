n=int(input())
for i in range(0, n+1):
    if i%2==0:
        continue
    else:
        if i%5==0:
            print(i)
