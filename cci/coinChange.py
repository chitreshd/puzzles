# Given a number N and set of distinct coins C, determine in how many ways N can be represented using distinct coins in coin set. 
# Example 1: For N=4 and C={1,2,3} there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3} , Ans: 4
# Example 2: For N=10 and C={2,5,3,6} there are five solutions: {2,2,2,2,2},{2,2,3,3},{2,2,6},{2,3,5},{5,5}., Ans: 5

# assume that denom_set is increasing sequence of denominations

def get_change(value, denom_index, denom_set, cache):

	# if denom_index >= 0:
	# 	print '[Internal] f({0},{1})'.format(value, denom_set[denom_index])
	# else:
	# 	print '[Internal] f({0},{1})'.format(value, 0)

	# base condition 1	
	if value == 0:
		return 1

	# base condition 2: this means we ran out of denominatons	
	if denom_index < 0:
		return 0

	denom = denom_set[denom_index]	
	ways = 0
		
	for i in range(value + 1):
		sub_value = value - i * denom
		if sub_value < 0:
			break

		# calculate next denomination to check in cache	
		if denom_index == 0:
			next_denom = 0
		else:
			next_denom = denom_set[denom_index - 1]

		sub_result = 0
		if (sub_value, next_denom) in cache:
			sub_result = cache[(sub_value, next_denom)]
		else:
			sub_result = get_change(sub_value, denom_index - 1, denom_set, cache)
			cache[(sub_value, next_denom)] = sub_result

		ways = ways + sub_result

	#print '[Internal] No of ways of getting change for value: {0} using denom {1} is {2}'.format(value, denom, ways)	
	return ways;

# denominatons = [1,2,3]
# value = 4
# ways = get_change(value, len(denominatons) - 1, denominatons, {})
# print 'No of ways of getting change for value: {0} is {1}'.format(value, ways)

# denominatons = [2,5,3,6]
# value = 10
# ways = get_change(value, len(denominatons) - 1, denominatons, {})
# print 'No of ways of getting change for value: {0} is {1}'.format(value, ways)

def start():
	value, denom_length = raw_input().split()
	value = int(value)
	denom_length = int(denom_length)

	denoms = raw_input().split()

	denom_set = []
	for i in range(denom_length):
		denom_set.append(int(denoms[i]))

	ways = get_change(value, denom_length - 1, denom_set, {})
	print 'No of ways of getting change for value: {0} is {1}'.format(value, ways)

start()
