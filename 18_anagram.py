print("Enter first string: ")
s1=input()
print("Enter second string: ")
s2=input()
l1=list(s1)
l2=list(s2)
l1.sort()
l2.sort()
if l1 == l2 :
    print("Anagram")
else:
    print("Not Anagram")
