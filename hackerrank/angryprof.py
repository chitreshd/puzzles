def check_threshold(entry):
	threshold = entry[0]
	arrivals = entry[1]
	num_of_pun_students = len(arrivals);
	
	for arrival in arrivals:
		if arrival > 0:
			num_of_pun_students = num_of_pun_students - 1

	if num_of_pun_students < threshold:
		print 'YES'
	else:
		print 'NO'

	
def start():
	num_of_cases = input('Number of cases: ');
	# Test case representation
	# Simplest can be array of tuples
	# [(threshold, [student_arrivals])]
	test_cases = []
	for i in range(0, num_of_cases):
		num_of_students, threshold = raw_input('Enter number of students and threshold: ').split()
		arrivals = [int(i) for i in raw_input('Enter the arrivals for each student: ').split()]
		
		if len(arrivals) != int(num_of_students):
			raise ValueError('Number of students should match the arrivals')
		
		test_cases.append((int(threshold), arrivals))

	for test_case in test_cases:
		check_threshold(test_case)

start()