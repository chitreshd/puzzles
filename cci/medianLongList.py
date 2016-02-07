"""
Define an algorithm to maintain a median when large number of numbers are given to the system.

Thoughts:
Median : For odd numbers its the middle number. For even numbers its the average of the middle
numbers.
Central idea: Find middle numbers.

1. Always keeping the list sorted, would make finding the media very easy. 
To sort the initial set of numbers, O(nlogn)
To maintain the sorted list, 
	- Find the space for the new number (log n)
	- Copy the left + number and right part of the list. (n)
	n + logn = O(n)
	Insertion is O(n) in time and space. 

2. Heaps:
maintain two heaps: min heap and max heap. Max heap can have one number more than min heap. 
Thus if two heaps are equal: min = avg(max_top + min_top)
Why heaps: Min heap will always keep the minimum number on top, so right side can be stored in min heap.
Max Heap will always keep the max number on top, so left side can be stored in max heap. 

How to decide, where a new number goes?
If the number <= median then it belongs to left side. Thus it will go in max heap
If the number > median then it belongs to right side. Thus it will go in min heap
maintain the constraint: max_heap - min_heap <= 1. Thus either both can have same size or max_heap will have one 
element more. 

Will need a class to maintain these two heaps as member variables
"""
import heapq
import random

class MedianMaintainer:
	"""docstring for MedianMaintainer"""
	min_heap = []
	max_heap = []			
	current_median = 999999

	def addToMinHeap(self, element):
		heapq.heappush(self.min_heap, element)

	def addToMaxHeap(self, element):
		inverted = -1 * element
		heapq.heappush(self.max_heap, inverted)

	def getMinTop(self):
		return self.min_heap[0]

	def getMaxTop(self):
		inverted = self.max_heap[0]
		return -1 * inverted

	def popMaxTop(self):
		inverted = heapq.heappop(self.max_heap)
		return ( -1 * inverted)

	def popMinTop(self):
		return heapq.heappop(self.min_heap)

	def add(self, element):
		if element <= self.current_median:
			self.addToMaxHeap(element)
		else:
			self.addToMinHeap(element)
		# rebalance
		# check whoose length is more. If its max_heap then by how much, if its min_heap, then push the element to max_heap. 
		# what are some preconditions: 
		if len(self.max_heap) < len(self.min_heap):
			heapq.heappush(self.max_heap, self.popMinTop())
		elif len(self.max_heap) - len(self.min_heap) > 1:
			heapq.heappush(self.min_heap, self.popMaxTop())

		if len(self.max_heap) > len(self.min_heap):
			self.current_median = self.getMaxTop()
		elif len(self.max_heap) == len(self.min_heap):
			self.current_median =  ( self.getMaxTop() + self.getMinTop() )/ 2
		else:
			print "Some issue with median maintainence"


medianManager = MedianMaintainer()

for i in xrange(10):
	random_number = random.randint(1,50)
	medianManager.add(random_number)
	
	print "Max heap: {1}	Min Heap: {0}	Current Median: {2}".format(medianManager.min_heap, medianManager.max_heap, medianManager.current_median)
	



			
