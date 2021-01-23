# Complete the checkMagazine function below.
def checkMagazine(magazine: list, note: list) -> str:
	my_dict = dict()
	for word in magazine:
		if word not in my_dict:
			my_dict[word] = 1
		else:
			my_dict[word]+=1
	for word in note:
		if word not in my_dict or my_dict[word] < 1:
			return "No"
		else:
			my_dict[word] -= 1
	return "Yes"

magazine = ["give", "me", "one", "grand", "today", "night"]
note = ["give", "one", "grand", "today"]


#checkMagazine(test,note)

assert(checkMagazine(magazine,note) == "Yes")

magazine = ["two", "times", "three", "is", "not", "four"]
note = ["two", "times", "two", "is", "four"]

assert(checkMagazine(magazine,note) == "No")

magazine = ["ive", "got", "a", "lovely", "bunch", "of", "coconuts"]
note = ["ive", "got", "some", "coconuts"]

assert(checkMagazine(magazine,note) == "No")