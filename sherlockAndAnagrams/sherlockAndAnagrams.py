# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
	res = 0
	my_dict = dict()
	my_list = list()
	for i in range(len(s)):
		for j in range(i+1,len(s) + 1):
			my_list = list(s[i:j].strip())
			my_list.sort()
			joined = ''.join(my_list)
			if joined in my_dict:
				res+=my_dict[joined]
				my_dict[joined]+=1
			else:
				my_dict[joined] = 1
	return res
s = "ifailuhkqq"
print(sherlockAndAnagrams(s))