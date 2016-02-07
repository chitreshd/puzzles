# For a given string and dictionary, how many sentences can you make from the string, such that all the words are contained in the dictionary. 

# // eg: for given string -> "appletablet" 
# // "apple", "tablet" 
# // "applet", "able", "t" 
# // "apple", "table", "t" 
# // "app", "let", "able", "t" 

# // "applet", {app, let, apple, t, applet} => 3 
# // "thing", {"thing"} -> 1

def findPossiSent(string, start, end, dictionary):

	print 'input: {0}	start: {1}	end: {2}'.format(string[start:end], start, end)
	if start >= end:
		return 1


	possibilities = 0;

	for i in range(start, end + 1):
		left_str = string[start:i]

		print 'Checking {0} from {1} to {2} [exclusive]'.format(left_str, start, i)
		if left_str in dictionary:
			right = findPossiSent(string, i, end, dictionary)
			possibilities += right
		

	return possibilities

dictionary = ['ab', 'c', 'd']
string = 'abcd'
print findPossiSent(string, 0, len(string), set(dictionary))

dictionary = ['app', 'let', 'apple', 't', 'applet']
string = 'applet'
print findPossiSent(string, 0, len(string), set(dictionary))

dictionary = ['thing']
string = 'thing'
print findPossiSent(string, 0, len(string), set(dictionary))

dictionary = ['app', 'let', 'apple', 't', 'applet']
string = 'applets'
print findPossiSent(string, 0, len(string), set(dictionary))
