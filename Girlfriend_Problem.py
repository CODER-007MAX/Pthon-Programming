#to input the coordinate of girlfriend's house.
n=int(input())

steps=0

if n >= 5:
    steps += (n//5)
    n = n%5
    
if n >= 4:
    steps += (n//4)
    n = n%4
    
if n >= 3:
    steps += (n//3)
    n = n%3
    
if n >= 2:
    steps += (n//2)
    n = n%2
    
steps += n

#to print the minimum number of steps.    
print(steps)
