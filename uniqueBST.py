class Solution:
    # @return an integer

    def numOfTree(self, lst):
    	if len(lst) == 0 or len(lst) == 1:
    		return 1
    	numsum = 0
    	for i in xrange(0, len(lst)):
    		numsum += self.numOfTree(lst[0:i]) * self.numOfTree(lst[i+1:len(lst)])

    	return numsum


    def numTrees(self, n):
    	nums = []
    	for i in xrange (1,n+1):
    		nums.append(i)

    	return self.numOfTree(nums)




s =Solution()
ret = s.numTrees(3)
print ret