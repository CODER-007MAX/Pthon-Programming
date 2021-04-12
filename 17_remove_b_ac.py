ONE = 1
TWO = 2

def toList(string):
	l = []
	for x in string:
		l.append(x)
	return l

def toString(l):
	return ''.join(l)

def stringFilter(string):

	state = ONE
	j = 0

	for i in range(len(string)):

		if state == ONE and string[i] != 'a' and string[i] != 'b':
			string[j] = string[i]
			j += 1

		if state == TWO and string[i] != 'c':
			string[j] = 'a'
			j += 1

			if string[i] != 'a' and string[i] != 'b':
				string[j] = string[i]
				j += 1

		state = TWO if string[i] == 'a' else ONE

	if state == TWO:
		string[j] = 'a'
		j += 1

	return toString(string[:j])

s1 = input()
string1 = stringFilter(toList(s1))
print (string1)

