"""
Problem: Given a number N, print all the possible valid pair combinations of paranthesis
Example: 
n = 1	()
n = 2 	()(), (())
n = 3	()()(), (())(), ()(()), ((()))
Solution:

Option 1:
Recursively build on n -1 cases
n = 1 () then n = 2 will be by inserting a new pair () at every possible positions in the Solution of n = 1
i.e. left ()(), middle (()), right ()()

This will generate lot of duplicates, which can be removed using HashSet. But still lot of time would be wasted in 
building these unwanted duplicates

Option 2:
build from scratch
when to add leftParenthesis and when to add rightParenthesis
leftParenthesis: if we have more available add leftParenthesis
rightParenthesis: if adding it wont cause syntax error
i.e. leftParenthesis used are greater than rightParenthesis
i.e. leftParenthesis left are less than or equal to rightParenthesis
n = 5, leftParenthesis used = 3, remaining = 2. So we can add, at max 3 rightParenthesis. Thus the remaining shuold be 3.
then we Recursively build the string for each position


0, [], [], 3, 3
	1, [(], [], 2, 3
		2, [((], [], 1, 3
			3, [(((], [], 0, 3
				4, [((()], [], 0, 2
					5, [((())], [], 0, 1
						6, [((()))], ["((()))"], 0, 0
			3, [(()], ["((()))"], 1, 2
				4, [(()(], [], 0, 2
					5, [(()()], [], 0, 1
						6, [(()())], ["((()))", "(()())"], 0, 0
				4, [(())], [], 1, 1
					5, [(())(], [], 0, 1
						6, [(())()], ["(())()"], 0, 0
		2, [()], [], 2, 2
			3, [()(], [], 1, 2
				4, [()((], [], 0, 2
					5, [()(()], [], 0, 1
						6, [()(())], ["((()))", "(()())", "()(())"], 0, 0
				4, [()()], [], 1, 1
					5, [()()(], [], 0, 1
						6, [()()()], ["((()))", "(()())", "()(())", "()()()", "(())()"], 0, 0


"""
def build(count, in_progress, combinations, leftParenthesis, rightParenthesis):
	if leftParenthesis < 0 or rightParenthesis < 0:
		return


	if leftParenthesis == 0 and rightParenthesis == 0:
		combinations.append(''.join(in_progress))
		return

	if leftParenthesis > 0:
		in_progress[count] = '('
		build(count + 1, in_progress, combinations, leftParenthesis - 1, rightParenthesis)

	if rightParenthesis > leftParenthesis:
		in_progress[count] = ')'
		build(count + 1, in_progress, combinations, leftParenthesis, rightParenthesis - 1)

	return		


def run(n):
	combinations = list()
	in_progress = ['' for x in xrange(n*2)]
	build(0, in_progress, combinations, n, n)
	print 'For n = {0} , combinations = {1}'.format(n, combinations)

for i in xrange(5):
	run(i)


