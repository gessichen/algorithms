class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
    	indexA = 0
    	indexB = 0
    	inserted_cnt = 0
    	while indexA < m + inserted_cnt and indexB < n:
    		num1 = A[indexA]
    		num2 = B[indexB]
    		if num2 < num1:
    			A.insert(indexA, num2)
    			indexA += 1
    			indexB += 1
    			inserted_cnt += 1
    		else:
    			indexA += 1

    	if indexB < n:
    		print B[indexB]
    		for i in xrange(indexB, n):
    			A.append(B[i])
    	return A




A = []
B = [1] 
s = Solution()
ret = s.merge(A,0,B,1)

print ret

