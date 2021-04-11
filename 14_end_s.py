s= input()
n = s.split()
print("Words ends with 's' are given below:\t")
for i in range(0, len(n)):
    if (n[i].endswith('s')):
        print(n[i])
    
