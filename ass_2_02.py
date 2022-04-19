def tostring(list):
    return ''.join(list)
def permute(a, l, r):
    if l==r:
        print (tostring(a))
    else:
        for i in range(l, r+1):
            a[1], a[i] = a[i], a[1]
            permute(a, 1+1, r)
            a[1], a[i] = a[i], a[1]
string=input()
n=len(string)
a=list(string)
permute(a, 0, n-1)
            
