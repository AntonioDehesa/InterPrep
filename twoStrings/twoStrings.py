# Complete the twoStrings function below.
def twoStrings(s1, s2):
	my_dict = dict()
	for element in range(len(s1)):
		if s1[element] not in my_dict:
			my_dict[s1[element]] = 1
	print(my_dict)
	for element in range(len(s2)):
		if s2[element] in my_dict:
			return "YES"
	return "NO"

s1 = "hello"
s2 = "world"
print(twoStrings(s1,s2))
assert(twoStrings(s1,s2) == "YES")
s1 = "hi"
print(twoStrings(s1,s2))
assert(twoStrings(s1,s2) == "NO")