def dtb(num):
    if num>=1:
        dtb(num//2)
    print(num % 2, end='')

dec=int(input())
dtb(dec)

