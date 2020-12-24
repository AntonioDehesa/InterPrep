# Complete the minimumBribes function below.
def minimumBribes(q: list):
    res = 0 
    q = [P-1 for P in q]
    for i,P in enumerate(q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            if q[j] > P:
            	res+=1
    print(res)


a = [5, 1, 2, 3, 7, 8, 6, 4]
print("Try a: ")
minimumBribes(a)
b = [1, 2, 5, 3, 7, 8, 6, 4]
#[0,1,4,2,6,7,5,3]
print("Try b:")
minimumBribes(b)