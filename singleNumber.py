class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        tmp = 0
        for i in xrange (0, len(A)):
        	tmp ^= A[i]

       	return tmp