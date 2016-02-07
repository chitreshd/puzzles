# find max profit 
# sample input: [10, 7, 5, 8, 11, 9]
# sample outout : 6

# Algorithm
# Start with min_price, max_price = s[0]
# for every current_price in s:
# 	if(min_price > current_price):
# 		min_price = current_price; // that means we think that we will be buying this stock
# 		max_price = min_price

# 	if(max_price < current_price):
# 		max_price = current_price

def get_max_profit(stock_prices):
	print("Input: " + str(stock_prices))
	max_price = stock_prices[0]
	min_price = stock_prices[0]

	for index in range(1, len(stock_prices)):
		current_price = stock_prices[index]
		if(min_price > current_price):
			min_price = current_price
			max_price = min_price

		if(max_price < current_price):
			max_price = current_price

	return (min_price, max_price)

print(get_max_profit([10, 7, 5, 8, 11, 9]))
print(get_max_profit([10, 7, 5]))