str=input()
dig=0
alp=0
spe=0
vow=0
for i in range(0, len(str)):
    ch=str[i]
    if (( ch>='A' and ch<='Z') or ( ch>='a' and ch<='z')):
        ch=ch.lower()
        if ( ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' ):
          vow+=1
        else:
          alp+=1
        
    elif ( ch>='0' and ch<='9'):
        dig+=1
    else:
     spe+=1
print("consonants are : ", alp)
print("digits are : ", dig)
print("special characters are : ", spe)
print("digits are : ", dig)
