# Given a series of stock values, come up with an optimized strategy to trade stock that will maximize the profits

def get_max_profit(price_list):
	profit = 0
	curr_max = -1

	for curr_price in reversed(price_list):
		if curr_price > curr_max:
			curr_max = curr_price

		profit = profit + ( curr_max - curr_price )

	return profit

def start():
	num_testcases = input()
	testcases = []

	for i in range(num_testcases):
		price_len = input()
		prices = raw_input().split()
		prices = [ int(price) for price in prices ]

		testcases.append(prices)

	for testcase in testcases:
		max_profit = get_max_profit(testcase)
		print max_profit

start()

#print get_max_profit([5,3,2])
#print get_max_profit([1,2,100])
#print get_max_profit([1,3,1,2])