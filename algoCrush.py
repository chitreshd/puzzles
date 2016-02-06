# Perform M operations on N numebrs

# Find a union of all the ranges
# If there is a number that occurs in every list, thats the max
import heapq

class Node(object):
	def __init__(self, input_tuple):
		super(Node, self).__init__()
		self.start = input_tuple[0]
		self.finish = input_tuple[1]
		self.weight = input_tuple[2]

	def __lt__(self, other):
		return self.finish < other.finish

	def __str__(self):
		return (self.start, self.finish, self.weight)

	def __repr__(self):
		return str((self.start, self.finish, self.weight))		

def findMax(array_of_nodes):
	heap = []
	array_of_nodes.sort(key = lambda node : node.start)
	#print 'sorted array: {0}'.format(str(array_of_nodes))
	curr_max = 0
	final_max = 0

	for node in array_of_nodes:

		#if len(heap) > 0:
			#print 'Heap: {0}'.format(heap)

		while len(heap) > 0 and heap[0].finish < node.start:
			popped = heapq.heappop(heap)
			curr_max = curr_max - popped.weight

		curr_max = curr_max + node.weight
		if curr_max > final_max:
			final_max = curr_max

		heapq.heappush(heap, node)

	return final_max

def start():
	N, M = raw_input().split()
	N = int(N)
	M = int(M)

	array_of_nodes = []

	for i in range(M):
		input_tuple = map(int, raw_input().split())
		node = Node(input_tuple)
		array_of_nodes.append(node)

	final_max = findMax(array_of_nodes)
	print final_max

start()