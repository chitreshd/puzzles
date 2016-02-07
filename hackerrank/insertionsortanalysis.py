# Counting number of swaps/shifts in a insertion sort. 
# There are two methods to solve it: Merge Sort and BIT. O(nlogn)
# - And offcourse Insertion Sort itself but it takes O(n^2)
#
# Modified Merge Sort:
# Inversion is defined as a case where L[i] > R[j] and i < j; where L is left and R is right array.
# In merge sort when can this inversion occur? When we are trying to merge two sorted arrays, for each L[i] > R[j]
# there is an inversion. 
# Hypothesis is that if sum of all the inversion counts for each stage is equal to total number of swaps during insertion sort
# on the same array. 
#
# Explanatory Note: When we do insertion sort, we are effectively merging right array of one element into left array. So the swap 
# number is associated with that element. But when we merge two arrays in merge sort and count inversions; since we are compairing
# left array elements, the inversion count gets associated with left array elements. This is little confusing, but with this tip
# when you try to anaylse an example, it should be make understanding the Hypothesis little easy.


def merge(left, right):
	print left
	print right
	merged = []
	i, j = 0,0
	while (i < len(left)) & (j < len(right)):
		if right[j] < left[i]:
			merged.append(right[j])
			j = j + 1
		else:
			merged.append(left[i])
			i = i + 1
	return merged

#def count_reqd_shifts_using_mdfd_merge_sort(input_array):
	# base case
	# get left
	# get right
	# recursion to merge
	

# def start():
# 	num_of_cases = input('Number of cases: ');
# 	test_cases = []
# 	for i in range(0, num_of_cases):
# 		num_of_elements = input('Enter expected number of elements in array: ')
# 		elements = [int(i) for i in raw_input('Enter the elements: ').split()]
		
# 		if len(elements) != int(num_of_elements):
# 			raise ValueError('Number of elements should match the expected number')
		
# 		test_cases.append((elements))

# 	print str(test_cases)

# 	for test_case in test_cases:
# 		count_reqd_shifts(test_case)


#start()

left = [2,4]
right = [1,3,5,7]

print merge(left, right)
