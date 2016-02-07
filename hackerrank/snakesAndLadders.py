# Snakes and ladders
from collections import deque

def finished(board_val):
	return board_val == 100

def overflow(board_val):
	return board_val > 100

def move(board_val, snakes_ladders):
	if board_val in snakes_ladders:
		return snakes_ladders[board_val]
	else:
		return board_val

def findMinSteps(snakes_ladders):
	step = 1
	visited = [False] * 110

	queue = deque()

	for dice_val in range(1,7):
		queue.append((1, dice_val, step))

	#print 'First dice_val set: ' + str(dice_val)

	while len(queue) > 0:
		board_val, dice_val, stepcount = queue.popleft()
		#print "{0}, {1}, {2}".format(board_val, dice_val, stepcount)

		board_val = move(board_val + dice_val, snakes_ladders)
		visited[board_val] = True

		if finished(board_val):
			#print "finished: stepcount: " + str(stepcount)
			return stepcount

		for next_dice_val in range(1,7):
			next_board_val = board_val + next_dice_val

			if not overflow(next_dice_val) and not visited[next_board_val]:
				queue.append((board_val, next_dice_val, stepcount + 1))

	return -1
		
		
def start():
	num_testcases = input()
	testcases = []

	for i in range(num_testcases):
		snakes_ladders = {}
		
		ladders = input()

		for i in range(ladders):
			ladder = raw_input().split()
			ladder_tup = [ int(l) for l in ladder]
			snakes_ladders[ladder_tup[0]] = ladder_tup[1]

		snakes = input()

		for i in range(snakes):
			snake = raw_input().split()
			snake_tup = [ int(l) for l in snake]
			snakes_ladders[snake_tup[0]] = snake_tup[1]

		testcases.append(snakes_ladders)

	for testcase in testcases:
		#print "Running: " + str(testcase)
		min_count = findMinSteps(testcase)
		print min_count

start()
#findMinSteps({})		
