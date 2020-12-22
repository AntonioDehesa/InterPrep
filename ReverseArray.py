# Complete the reverseArray function below.
def reverseArray(a):
    return a[::-1]

test_array = [1,2,3]
print("Test Array: {}".format(test_array))
res_array = reverseArray(test_array)
print("Result Array: {}".format(res_array))
reversed_array = list(reversed(test_array))
print("Reversed Array: {}".format(reversed_array))
assert(reversed_array == res_array)