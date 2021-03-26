#To Input the total number of Pieces of Cake
n=int(input())

#input to find for cherry piece or not
p = list(input().split()) 

s = ''
n2 = s.join(p)
print(round(int(n2, 2)/n))
