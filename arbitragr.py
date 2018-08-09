import requests
from bs4 import BeautifulSoup
import re

# Function that takes an exchange rate matrix and finds the most profitable trade path,
# if there is one.
def arbitrage(matrix):
	# Makes sure matrix is valid
	if any([i <= 0 for row in matrix for i in row]):
		print("Invalid matrix")
		return None

	candidates = []
	highest = 0
	n = range(len(matrix))

	# Takes a starting point and a path then adds that path and it's profitability to
	# candidates, if it's profitable and more profitable than any of the other candidates
	def bigger (lst, origin):
		nonlocal candidates
		nonlocal highest
		if lst:
			lst = [origin] + lst + [origin]
			start = 100
			current = start
			for i, n in enumerate(lst):
				if i != 0:
					current *= matrix[n][lst[i - 1]]
			if current > start and current > highest:
				highest = current
				candidates.append((current, lst))

	# neighbors[i] is a list of all numbers in n (total number of currencies) not equal to i
	neighbors = [[i for i in n if i != v] for v in n]

	# Recursively checkes all non-looping paths from a given starting point
	def check_node(path, val, origin):
		bigger(path, origin)
		for i in neighbors[val]:
			if i not in path and i != origin:
				check_node(path + [i], i, origin)

	# Checks every possible path starting from each node possible from the list
	for i in n:
		check_node([], i, i)

	# Gets the maximum of all the candidates then prints the respective path
	if candidates:
		result = max(candidates, key=lambda e: e[0])
		print("The highest percentage return you will be able to make is {:.3f}% by trading your currency in the following sequence: {}".format(result[0] - 100, [currencies[i] for i in result[1]]))
	else:
		print("There is no profitable trade path with the given currencies. ")

# Has following structure (for below):
#                          
#                           From currencies:
#             
#                         |  0  |  1  |  2  |
#                   ______|_AAA_|_BBB_|_CCC_|
#                   0 AAA |     |     |     |
#                   ______|__1__|_.25_|__4__|
#                   1 BBB |     |     |     |
#  To currencies:   ______|_.1__|__1__|__3__|
#                   2 CCC |     |     |     |
#                   ______|__2__|_.5__|__1__|
#
# So, for example, you could trade in 1 AAA for 2 CCC
# or .1 BBB


# Given a list of currencies, returns a currency exchange matrix
# See above for a horrible ASCII art example
def find_arbitrage(currencies):
	n = range(len(currencies))

	# Initializes matrix
	matrix = [[-1 for j in n] for i in n]

	# Requests trading price for each currency on the matrix
	for i, currency in enumerate(currencies):
		r = requests.get("http://x-rates.com/table/", params={"from": currency, "amount": "1"})
		soup = BeautifulSoup(r.content, "html.parser")
		frm = "from=" + currency

		# Uses parser to get trade data between that currency and 
		# each other currency in the list
		for j, other in enumerate(currencies):
			if other != currency:
				conversion = soup.find("a", href=(re.compile(frm) and re.compile("to=" + other)))
				if conversion:
					matrix[j][i] = float(conversion.text)
			else:
				matrix[j][i] = 1
	return matrix

currencies = ["NZD", "JSY", "USD", "EUR"]

arbitrage(find_arbitrage(currencies))
