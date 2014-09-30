class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
    	maxsum = 0
    	current = 0
    	maxval = float("-inf")

    	for i in xrange(0, len(A)):
    		if A[i] > maxval:
    			maxval = A[i]
    		current += A[i]
    		if current < 0:
    			current = 0
    		elif current > maxsum:
    			maxsum = current 


    	if maxsum == 0:
    		if maxval < 0:
    			maxsum = maxval


    	return maxsum

s = Solution()
ret = s.maxSubArray([-2,-2,-5,5])

print ret