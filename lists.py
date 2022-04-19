l=[]
n=int(input())

for  i in range(n):
    a=input().split()
    
    for i in range(1, len(a)):
        a[i]=int(a[i])
        
    if a[0] == "insert":
        l.insert(a[1], a[2])
        
    elif a[0] == "append":
        l.append(a[1])
        
    elif a[0] == "remove":
        l.remove(a[1])
        
    elif a[0] == "sort":
        l.sort()
        
    elif a[0] == "pop":
        l.pop(a[1])

    elif a[0] == "reverse":
        l.reverse()
        
    if a[0] == "print":
        print(l)
        
    
