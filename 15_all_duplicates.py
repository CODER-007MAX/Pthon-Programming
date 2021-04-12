s = input()
s = list(s)
s1 = []
s2 = []
for i in s:
    if i not in s1:
        s1.append(i)
    else:
        if i not in s2:
            s2.append(i)
print("All the repeating elements are: ", end = "")
print(", ".join(s2))
