B = [ 1, 2, 3 ,4, 5, 6, 7, 9, 10]


def find_max(C):
	print(find_(C, 0, len(C)-1 ))


def find_(A, start, end, max=-1):
	if start>end:
		return max

	middle = int((start+end) / 2)
	if A[middle] > max:
		max = A[middle]
	if A[start]>A[middle]:
		return find_(A, start, middle-1, max)
	else:
		return find_(A, middle+1, end, max)



# for i in range(len(B)):
# 	C = B[i:] + B[:i]
# 	find_max(C)
C = B[4:] + B[:4]
find_max(C)

# complexity log(n) base 2. ( modified binary search )