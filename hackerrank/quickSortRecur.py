# Implement quick sort using the recursive approachh

# Using Lomotu Parition scheme by chooosing last element as a pivot

def myprint(arr):

	s = ''

	for i in arr:
		s = s + str(i) + ' '

	print s



def partition(input_arr, lo, hi):
	pivot = input_arr[hi]
	# place for swapping
	i = lo 
	for j in range(i, hi):
		if input_arr[j] <= pivot:
			input_arr[i], input_arr[j] = input_arr[j], input_arr[i]
			i = i + 1
			#print "Swapped [ (i,j) = ({0},{1}) ] {2}".format(i,j,input_arr)

	input_arr[i], input_arr[hi] = input_arr[hi], input_arr[i]
	return i

def quickSort(input_arr, lo, hi):
	if lo < hi:
		p = partition(input_arr, lo, hi)
		myprint(input_arr)
		quickSort(input_arr, lo, p - 1)
		quickSort(input_arr, p + 1, hi)


def start():
	arr_length = input()
	arr = raw_input().split()
	arr = [int(j) for j in arr]
	quickSort(arr, 0, len(arr) - 1)
	#print "Sorted array: {0} ".format(arr)

start()


