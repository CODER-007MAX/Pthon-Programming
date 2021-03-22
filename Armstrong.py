a=input()
ln=len(a)
s=0
for i in a:
    s+=int(i)**ln
if int(a)==s:
    print('number is armstrong')
else:
    print('not armstrong')
