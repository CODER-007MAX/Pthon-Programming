n=int(input())
count=0
rem=0
while n>0:
    rem=n%10
    count = count+rem
    n=n//10
print(count)
