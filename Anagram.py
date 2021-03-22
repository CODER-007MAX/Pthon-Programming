n1=input()
n2=input()
list1=list(n1)
list1.sort()
list2=list(n2)
list2.sort()
if list1==list2:
    print('Anagram')
else:
    print('Not Anagram')
