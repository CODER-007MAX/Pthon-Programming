n = int(input())
x = []
for i in range(n):
    y = int(input())
    x.append(y)
for i in range(len(x)):
    me = 0
    you = x[i] + 1
    if x[i]%2 != 0:
        for j in range(x[i]):
            me += 1
            you -= 1
            if me == you:
                print(me)
            elif you == me:
                print(you)
