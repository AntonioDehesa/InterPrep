# Complete the minimumSwaps function below.
def minimumSwaps(arr: list):
	res = 0
	arr = [P-1 for P in arr]
	sortedList = sorted(arr)
	while arr != sortedList:
		for i,q in enumerate(arr):
			if i != q:
				arr[i],arr[q] = arr[q],arr[i]
				res+=1
	return res

test = [7,1,3,2,4,5,6]
assert(minimumSwaps(test) == 5)
print(minimumSwaps(test))
test2 = [2,3,4,1,5]
assert(minimumSwaps(test2) == 3)
print(minimumSwaps(test2))