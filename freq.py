word = input()
word = word.lower()
print({x:word.count(x) for x in 'abcdefghijklmnopqrstuvwxyz'})
