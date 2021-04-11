print('Enter the string: ')
s = input()
k = list(s)
t = len(s)
print('Enter the number of required parts:')
n = int(input())
for i in range(0, t):
    print(k[i], end='')
    if ((i+1)%n==0) :
        print(' ')
