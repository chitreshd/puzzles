#1,1,2,3,5,8..

def fibo(n, a):
	if n in a:
		return a[n]

	if n <= 1:
		a[n] = 1
		return a[n]

	a[n] = fibo(n - 1, a) + fibo(n - 2, a)
	return a[n]

def fiboPrint(n):
	a = {}
	fibo(n, a)
	return a.values()


for i in xrange(10):
	print '{0}th fibo number: {1}'.format(i, fiboPrint(i))



"""
n = 1
f(1) = 1

n = 5
f(5) : 8
	f(4) : 5
		f(3) : 3
			f(2) : 2
				f(1) : 1
				f(0) : 1
			f(1) : 1
		f(2) : 2
	f(3) : 3
"""