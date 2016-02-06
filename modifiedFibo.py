# Modified fibonacci

def modified_fibbo(a,b,n):

	curr_1 = b;
	curr_2 = a;

	curr = -1	

	for i in range(2,n):
		#print 'Before [Term: {0}] curr: {1} curr_1: {2} curr_2: {3}'.format(i, curr, curr_1, curr_2)
		curr = curr_1 * curr_1 + curr_2
		curr_2 = curr_1
		curr_1 = curr
		#print 'After [Term: {0}] curr: {1} curr_1: {2} curr_2: {3}'.format(i, curr, curr_1, curr_2)
	return curr


a,b,n = raw_input().split();
a = int(a)
b = int(b)
n = int(n)
ans = modified_fibbo(a,b,n)
print ans
