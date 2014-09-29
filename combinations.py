class Solution:
    # @return a list of lists of integers
    def getCombinations (self, n, k, lst, index, num, retlst):
    	if index == k - 1:
    		newlst = lst[:]
    		newlst.append(num)
    		retlst.append(newlst)
    	else:
    		lst.append (num)
    		for i in xrange (num + 1, n - k + index + 3):
    			self.getCombinations(n,k,lst,index+1,i,retlst)
    		lst.pop()	

    def combine(self, n, k):
    	retlst = []
    	for i in xrange (0, n - k + 1):
    		self.getCombinations(n,k,[],0,i+1,retlst)
    	return retlst


s = Solution()
s.combine(4,3)