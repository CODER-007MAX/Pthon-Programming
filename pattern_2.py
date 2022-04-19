r = int(input())
c = int(input())
y = r//2
z = c//2
for i in range(r):
        if i==0 :
            print(" "*(z-i), end = '')
            print("*")
        elif i<=y and i!=0:
            print(" "*(z-(i+2)), end = '')
            print("*"*(i+2))
        elif i>y and i!=r-1:
            print(" "*(z-(r-i)), end = '')
            print("*"*(r-i))
        elif i==r-1 :
            print(" "*(z-1), end = '')
            print("*")
