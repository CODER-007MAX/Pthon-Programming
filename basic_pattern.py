r = int(input())
a = round(r/2)
for i in range(1, r+1):
    if i <= r//2:
       print("*"*i)
    else:
        if(r%2 == 0):
             print("*"*(r-i))
        else:
            print("*"*((r+1)-i))
