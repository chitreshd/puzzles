# Sherlock Min Max
import bisect
import sys

def findMin(number, array, high, low):
	#print 'Now processing array from {0} to {1} for number: {2}'.format(low, high, number)
	if low > high:
		# base condiftion
		return (-1, -1)

	mid = ( high + low ) / 2
	mid_num = array[mid]

	# check for the indices
	curr_diff = abs(number - mid_num)

	tupples = []
	tupples.append((curr_diff, mid))
	# check if left exists
	left = mid - 1

	if left >= 0:
		left_diff = abs(number - array[left])
		tupples.append((left_diff, left))

	# check if right exists
	right = mid + 1
	if right <= high:
		right_diff = abs(number - array[right])
		tupples.append((right_diff, right))

	min_diff_tupple = min(tupples, key=lambda i: i[0] )


	if min_diff_tupple[1] == mid:
		# found our guy
		#print 'Found min for number: {0} and its {1}'.format(number, min_diff_tupple)
		return (min_diff_tupple[0], mid_num)

	if min_diff_tupple[1] == left:
		return findMin(number, array, left, low)

	if min_diff_tupple[1] == right:
		return findMin(number, array, high, right)

# arr = [5,8,14]
# print findMin(4, arr, len(arr) - 1, 0)
# print findMin(5, arr, len(arr) - 1, 0)

# arr = [3, 12, 15, 19, 24, 34, 42]
# print findMin(32, arr, len(arr) - 1, 0)
# print findMin(100, arr, len(arr) - 1, 0)
# print findMin(1, arr, len(arr) - 1, 0)

def getInsetionPoint(array, x):
	return bisect.bisect_left(array, x)

def findMinieMax2(array, P, Q):

	array.sort()
	
	p_index = getInsetionPoint(array, P)
	q_index = getInsetionPoint(array, Q)
	length =  len(array)
	
	min_max = -sys.maxint - 1
	ans = 0

	if array[p_index] != P:
		
		mid_at_p_index = ( ( array[p_index - 1] + array[p_index] ) / 2 )
		if p_index == 0 or P >  mid_at_p_index:
			min_max = array[p_index] - P
			ans = P
		else :
			p_index = p_index - 1
	
	if q_index == length or ( array[q_index] != Q and (Q < ( array[q_index - 1] + array[q_index] ) / 2 ) ):
		print 'came inside, q_index: {0}'.format(q_index)
		curr_min_max = Q - array[q_index - 1]
		if curr_min_max > min_max:
			min_max = curr_min_max
			ans = Q
		q_index = q_index - 1

	print 'p_index : {0}	q_index: {1}'.format(p_index, q_index)
	while p_index < q_index:
		curr_min_max = ( array[p_index + 1] - array[p_index] ) >> 1
		print 'curr_min_max: {0}	min_max: {1}	i: {2}	array[i]: {3}'.format(curr_min_max, min_max, p_index, array[p_index])
		if curr_min_max > min_max:
			min_max = curr_min_max
			ans = array[p_index] + curr_min_max
		p_index = p_index + 1
	return ans


def findMinieMax(array, P, Q):
	origP = P
	origQ = Q
	array.sort()

	arrayLength = len(array)

	# bound P and Q
	P = max(P, array[0])
	Q = min(Q, array[arrayLength - 1])
	bounded = [i for i in range(P, Q + 1)]
	arrB = []
	arrB.append(origP)
	arrB.extend(bounded)
	arrB.append(origQ)
	#print 'before sorting: ' + str(array)
	
	#print 'after sorting: ' + str(array)
	maxie_tupple = (0,0)

	for b in arrB:
		min_tupple = findMin(b, array, arrayLength - 1, 0)
		
		min_diff = min_tupple[0]
		if min_diff > maxie_tupple[0]:
			# found another max
			maxie_tupple = (min_diff, b)

	return maxie_tupple


def start():
	n = input()
	arr = raw_input().split()
	arr = [ int(j) for j in arr]
	p, q = raw_input().split()
	p = int(p)
	q = int(q)
	diff_tupple = findMinieMax2(arr, p, q)
	print diff_tupple

start()
# arr = [5,8,14]
# print 'Sherlock found: ' + str(findMinieMax(arr, 4, 9))


# arr = [5,8,9]
# print 'Sherlock found: ' + str(findMinieMax2(arr, 6, 9))
# print 'Sherlock found: ' + str(findMinieMax2(arr, 4, 9))

# arr = [5,8,14]
# print 'Sherlock found: ' + str(findMinieMax2(arr, 4, 9))
