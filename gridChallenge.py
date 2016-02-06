# Grid challenge
# Given a grid, evaluate if it can be lexically sorted

def sortRow(matrix, row_index):
	row = matrix[row_index]
	row.sort()


def canGridBeSorted(matrix):
	for row_index in range(len(matrix)):
		sortRow(matrix, row_index)
		if row_index == 0:
			continue

		row_length = len(matrix[row_index])
		for j in range(row_length):
			if matrix[row_index - 1][j] > matrix[row_index][j]:
				return 'NO'

	return 'YES'


def start():
	num_testcases = input()
	testcases = []

	for i in range(num_testcases):
		
		length = input()
		matrix = []

		for i in range(length):
			row = raw_input()
			row = row.strip()
			matrix.append(list(row))


		testcases.append(matrix)

	for testcase in testcases:
		#print "Running: " + str(testcase)
		result = canGridBeSorted(testcase)
		print result


start()