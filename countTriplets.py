def countTriplets(arr,r):
	count = 0
	dictNums = dict()
	dictPairs = dict()
	for i in reversed(arr):
		count+=dictPairs.get(i*r,0)
		if i*r in dictNums:
			dictPairs[i] = dictPairs.get(i,0) + dictNums[i*r]
		dictNums[i] = dictNums.get(i,0) + 1
	return count
arr = [1,4,16,64]
r = 4
print(countTriplets(arr, r))
assert(countTriplets(arr,r) == 2)
arr = [1,2,2,4]
r = 2
print(countTriplets(arr,r))
assert(countTriplets(arr,r) == 2)
arr = [1, 3, 9, 9, 27, 81]
r = 3
print(countTriplets(arr,r))
assert(countTriplets(arr,r) == 6)
arr = [1] * 100
r = 1
print(countTriplets(arr,r))
assert(countTriplets(arr,r) == 161700)
arr = [1,2,1,2,4]
r = 2
print(countTriplets(arr,r))
assert(countTriplets(arr,r) == 3)