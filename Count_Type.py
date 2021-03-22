str=input()
dig=0
alp=0
spe=0
for i in range(0, len(str)):
    ch=str[i]
    if ( ch>='A' and ch<='Z'):
        alp = alp+1
    elif ( ch>='a' and ch<='z'):
        alp+=1
    elif ( ch>='0' and ch<='9'):
        dig+=1
    else:
     spe+=1
print("alphabets are : ", alp)
print("digits are : ", dig)
print("special characters are : ", spe)
