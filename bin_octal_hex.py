def print_formatted(number):
  l = []
  for j in range(1, n+1):
        l.append(len(list(bin(j))))
  y = max(l)
  for i in range(1, n+1):
      
        if len(str(i)) == 1:
            print(" ", end = '')
        else:
            print("", end = '')
        print(i, end = '  ')

        
        s = list(oct(i))
        s.pop(0)
        s.pop(0)
        if len(s) == 3:
            print("", end = '')
            print(s[-3], end = '')
            print(s[-2], end = '')
            print(s[-1], end = '')
        if len(s) == 2:
            print(" ", end = '')
            print(s[-2], end = '')
            print(s[-1], end = '')
        if len(s) == 1:
            print("  ", end = '')
            print(s[-1], end = '')

        if len(hex(i)) == 4:
           print(" ", end = '')
           print(((hex(i).replace("0x", ""))).upper(), end ='')
        if len(hex(i)) == 3:
           print("  ", end = '')
           print(((hex(i).replace("0x", ""))).upper(), end ='')
        if len(hex(i)) == 2:
           print("   ", end = '')
           print(((hex(i).replace("0x", ""))).upper(), end ='')

        x = len(list(bin(i)))
        if (x > 0):
            print(" "*(y-(x-1)), end = '')
            print(eval(bin(i).replace("0b", "")), end = '  ')

        print('\n', end = '')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
