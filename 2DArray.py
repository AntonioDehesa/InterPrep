# Complete the hourglassSum function below.
def hourglassSum(arr):
	results = list()
	for rows in range(4):
		for cols in range(4):
			a = arr[rows][cols:3+cols]
			b = arr[rows+1][1 + cols]
			c = arr[rows+2][cols:3+cols]
			res = 0
			for i in a:
				res+=i
			res+=b
			for i in c:
				res+=i
			results.append(res)
	return max(results)


arr = [[-9,-9,-9,1,1,1],[0,-9,0,4,3,2],[-9,-9,-9,1,2,3],[0,0,8,6,6,0],[0,0,0,-2,0,0],[0,0,1,2,4,0]]
res_hourglass = hourglassSum(arr)
print(res_hourglass)
assert(res_hourglass == 28)