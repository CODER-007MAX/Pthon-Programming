n  = int(input())
m = n//2
for i in range (1, n+1, 2):
    print(" "*(n-i), end = ' ')
    print("*"*(i))
for i in range(n+1, 0, -2):
    print(" "*(n-i), end = ' ')
    print("*"*i)
