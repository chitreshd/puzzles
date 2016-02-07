from collections import deque

def findKthMagicNumber(k):
	# define queues
	q_3 = deque([1])
	q_5 = deque([1])
	q_7 = deque([1])
	magicnumbers = []

	while k > 0:

		min_of_all = min(q_3[0], q_5[0], q_7[0])

		if min_of_all == q_3[0]:
			q_3.popleft()

		if min_of_all == q_5[0]:
			q_5.popleft()

		if min_of_all == q_7[0]:
			q_7.popleft()

		if len(magicnumbers) == 0 or ( len(magicnumbers) > 0 and min_of_all != magicnumbers[-1] ) :
			magicnumbers.append(min_of_all)
			q_3.append(min_of_all * 3)
			q_5.append(min_of_all * 5)
			q_7.append(min_of_all * 7)

		k -= 1

	return magicnumbers

print 'Magic numbers till 1: {0} '.format(findKthMagicNumber(1))
print 'Magic numbers till 5: {0} '.format(findKthMagicNumber(5))
print 'Magic numbers till 10: {0} '.format(findKthMagicNumber(10))

"""
f(3):
	k = 3 q_3 = [1], q_5 = [1], q_7 = [1], magicnumbers = [] min_of_all = 1, 
	k = 2 q_3 = [3], q_5 = [5], q_7 = [7], magicnumbers = [1] min_of_all = 3, 
	k = 2 q_3 = [9], q_5 = [5, 15], q_7 = [7, 21], magicnumbers = [1, 3] min_of_all = 5,
	
"""



