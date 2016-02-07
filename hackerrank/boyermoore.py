# Boyer Moore Algorithm


# def goodSuffixRule():
	
# def badCharRule():

def calculateCharOccur(pattern):
	charOccurDict = {}
	index = 0
	for char in pattern:
		charOccurDict[char] = index
		index += 1

	return charOccurDict

def getShiftDistance(charOccurDict, char):
	if char in charOccurDict:
		return charOccurDict[char]
	else:
		return -1

def substr(text, pattern):
	charOccurDict = calculateCharOccur(pattern)
	patLength = len(pattern)
	i = 0
	j = patLength - 1



	while j >= 0:
		if (i + j) >= len(text):
			# couldnt find the pattern. recahed end of text
			return -1

		if pattern[j] == text[i + j]:
			# match
			j -= 1
			continue
		else:
			# mismatch
			shift_distance = getShiftDistance(charOccurDict, text[i + j])

			if j < shift_distance:
				i += 1
			else:
				i = i + ( j - shift_distance)

			j = patLength - 1

	return i


print substr('abcdbar', 'bar')
print substr('abcdbar', 'bart')