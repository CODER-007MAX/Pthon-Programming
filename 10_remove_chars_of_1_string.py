s = input()
s = list(s)
s1 = input()
s1 = list(s1)
string = []
for i in range(0, len(s)):
        if (s[i] in s1):
            s1.remove(s[i])
            for j in range (0, len(s1)):
                if s[i] in s1:
                    s1.remove(s[i])
            
print("".join(s1))

        
       
