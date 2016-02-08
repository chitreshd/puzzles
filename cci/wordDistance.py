"""
Given a large file, write an algorithm to find minimum distance between two words in that file.

Write a class that gets initialized by file object
Initializer will tokenize these files into seprate words

Required Functions 
-tokenize
-merge: to merge two array objects
-findDistance: to find the distance

algorithm:
preprocessing: create an inverted index of all the words.
When given two words, fetch the list of occurrences about the words. 
merge two lists with each number being suffixed as A and B. 
find two closest occurrences -- key thing.

Brainstorming
this is not correct that is boring 

1a 2b 3a 5b
1a 2a 3a 10b 11a 12b

Track succsive types and indexes
"""

class WordDistanceCounter():
	"""docstring for WordDistanceCounter"""
	def __init__(self):
		self.fileA_words = []
		self.fileB_words = []

	def initialize(self, file_location):
		file_obj = open(file_location,'r')
		text = file_obj.read()
		self.inverted_index = self._index(text)

	def find_min_distance(self, wordA, wordB):
		if wordA in self.inverted_index and wordB in self.inverted_index:
			merged_list = self._merge(self.inverted_index[wordA], self.inverted_index[wordB])
			return self._find_close_match(merged_list)[0]
		else:
			return -1
	def _index(self, large_text):
		inverted_index = {}
		for index, element in enumerate(large_text.split()):
			if element in inverted_index:
				occurrences = inverted_index[element]
				occurrences.append(index)
			else:
				inverted_index[element] = [index]

		return inverted_index

	def _merge(self, list_a, list_b):
		pointer_a = 0
		pointer_b = 0
		merged = []

		while pointer_a < len(list_a) and pointer_b < len(list_b):
			if list_a[pointer_a] < list_b[pointer_b]:
				merged.append((list_a[pointer_a],'a'))
				pointer_a += 1
			else:
				merged.append((list_b[pointer_b],'b'))
				pointer_b += 1

		while pointer_a < len(list_a):
			merged.append((list_a[pointer_a],'a'))
			pointer_a += 1

		while pointer_b < len(list_b):
			merged.append((list_b[pointer_b],'b'))
			pointer_b += 1		
		
		return merged

	def _find_close_match(self, merged_list):
		min_dist = 999999
		location_1 = ()
		location_2 = ()

		for i in xrange(1, len(merged_list)):
			last = merged_list[i - 1]
			curr = merged_list[i]

			if last[1] != curr[1]:
				dist = curr[0] - last[0]

				if dist < min_dist:
					min_dist = dist
					location_1 = last
					location_2 = curr

		return (min_dist, location_1, location_2)


distanceCounter = WordDistanceCounter()
merged_list_1 = [(1,'a'), (2,'b') , (3,'a'), (5,'b')]
merged_list_2 = [(1,'a'), (2,'a'), (3,'a'), (10,'b'), (11,'a'), (12,'b')]

print distanceCounter._find_close_match(merged_list_1)
print distanceCounter._find_close_match(merged_list_2)
print distanceCounter._merge([1,3],[2,5])
print distanceCounter._merge([1,2,3,11],[10,12])
print distanceCounter._index('this is large this is small that is not so small')
print "Now testing end to end functionality"
file_location = "./data/sample.txt"
distanceCounter.initialize(file_location)
print "Min distance between is and so: {0}".format(distanceCounter.find_min_distance("is","so"))



