n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
sum=n1+n2+n3+n4
for i in range(sum):
    if i==n1 or i==n2 or i==n3 or i==n4:
        large=i
print(large)
