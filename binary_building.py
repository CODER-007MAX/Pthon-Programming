'''
n=int(input())
list1 = []
t = int()
for j in range (1, n+1):
    dtb(j//2)
    list1.append(j%2)
    list1 = [str(i) for i in list1]
    t = int("".join(list1))
    print("%4d"%t)
    j+=1
'''
n = int(input())
h = len(str(bin(n))[2:])
    
for k in range(n+1):
    tt = str(bin(k))[2:]
    p = len(tt)
    print(''*(h-p)+tt)
