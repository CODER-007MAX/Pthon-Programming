for i in range (int(input())):
    tot = 0
    D, d, p, q = map(int, input().split())
    if d<=D and D<=100:
        tot = d*p
        D = D - d
        while(D!=1):
            tot += (p+q)*2
            p = p+q
            D = D-2
        if D==1:
            p = p+q
            tot += p
        print(tot)
