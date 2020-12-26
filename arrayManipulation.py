# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arrToWork = [0] * (n + 1)
    res = arrToWork
    for a,b,k in queries:
        arrToWork[a-1] += k#This stablishes the slope of the sums.
        arrToWork[b] -= k	#this indicates the disminution  of the slope
    max_value = 0
    running_count = 0
    for i in arrToWork:
        running_count += i
        if running_count > max_value:
            max_value = running_count
    return max_value

queries = [[1,5,3],[4,8,7],[6,9,1]]
n = 10
print(arrayManipulation(n,queries))

queries = [[2, 6, 8,],
		  [3, 5, 7],
		  [1, 8, 1],
		  [5, 9, 15]]
n = 10
print(arrayManipulation(n,queries))

n = 5
queries = [[1,2,100],[2,5,100],[3,4,100]]
print(arrayManipulation(n,queries))