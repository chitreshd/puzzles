import sys

def factorial(n):
	# Lets calculate factorial
	# fact(n) = n * (n - 1) * (n-2) * (n - 3) .... * 1
	result = 1
	for i in range(1, n):
		result = result * i

	return result
	
n = int(sys.argv[1])
print 'factorial for ' + str(n) + ' : ' + str(factorial(n))