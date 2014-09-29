class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if prices == None:
            return 0
        bought = False
        profit = 0
        for i in xrange (0, len(prices) - 1):
        	if prices[i + 1] > prices[i] and bought == False:
        		low = prices[i]
        		bought = True

        	elif prices[i + 1] < prices[i] and bought == True:
        		profit += (prices[i] - low)
        		bought = False

        if bought == True:
        	profit += (prices[len(prices) - 1] - low)

        return profit