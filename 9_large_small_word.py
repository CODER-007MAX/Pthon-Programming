# Program to print the longest and the shortest word of a string -
string = input()
list1 = string.split()
list2 = []

for i in range(0, len(list1)):
    x = len(list1[i])
    list2.append(x)         # To make a list of index values of the string -

short_element = list2.index(min(list2))
long_element = list2.index(max(list2))


# To print the longest and the shortest elements of the string -
print("Minimum length word is : ", list1[short_element])
print("Maximum length word is : ", list1[long_element])



