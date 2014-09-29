class Solution:
    # @return a list of integers


    def buildRow(self, currow, rowIndex, lst):
#    	print currow

    	if currow == rowIndex:
    		return lst

    	for i in xrange (0, len(lst) - 1):
    		lst[i] = lst[i] + lst[i + 1]

    	lst[len(lst) - 1] = 1
    	lst.insert(0,1)

#    	print lst

    	return self.buildRow(currow + 1, rowIndex, lst)


    def getRow(self, rowIndex):
    	return self.buildRow(0,rowIndex,[1])


s = Solution()

ret = s.getRow(3)

print ret