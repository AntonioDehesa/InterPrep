# Complete the rotLeft function below.
def rotLeft(a: list, d: int):
	for i in range(d):
		a.append(a.pop(0))
	return a

gg = [1,2,3,4,5]
res = rotLeft(gg, 4)
print(res)