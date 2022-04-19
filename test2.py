arr = list(map(str, input().strip('[]').split(', ')))
varr = []
c1 = arr.count('"R"')
varr.append(c1)
c2 = arr.count('"G"')
varr.append(c2)
c3 = arr.count('"B"')
varr.append(c3)
print(varr)
'''
if (max(arr) == varr[0]):
    print('"R"')
if (max(arr) == varr[1]):
    print('"G"')
if (max(arr) == varr[2]):
    print('"B"')

'''
