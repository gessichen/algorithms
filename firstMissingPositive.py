class Solution:
    # @param A, a list of integers
    # @return an integer

    def swap (self,A,i,j):
    	tmp = A[i]
    	A[i] = A[j]
    	A[j] = tmp

    def firstMissingPositive(self, A):
    	i = 0
    	l = len(A) - 1
    	while (i <= l):
    		if A[i] <= 0:
    			self.swap(A,i,l)
    			l -= 1
    		else:
    			i+=1

#    	print l
    	
    	for i in xrange (0, l + 1):
    		a = A[i]
    		absa = abs(a)
    		print absa
    		if absa <= l + 1:
    			A[absa - 1] = -abs(A[absa - 1])

    	print A

    	for i in xrange(0, l + 1):
    		if A[i] > 0:
    			return i + 1
    	return l + 2


lst = [2,2,1,3]
s = Solution()
ret = s.firstMissingPositive(lst)
print ret
