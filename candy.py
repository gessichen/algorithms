class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):

    	if ratings == None:
    		return 0

        candies = [1]
        for i in xrange (1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
        		candies.append(candies[i - 1] + 1)
            else:
                candies.append(1)

#        print candies
        candySum = candies[len(ratings) - 1]

        for i in xrange (len(ratings) - 2, -1, -1):
        	if ratings[i] > ratings[i+1]:
        		candies[i] = max(candies[i+1] + 1, candies[i])
        	candySum += candies[i]	

        return candySum

s = Solution()

ret = s.candy([1,2])

print ret