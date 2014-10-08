class Solution:
    # @return a list of lists of string
    def contradict(self, row, col, lst):
#    	print lst
    	for i in xrange(0, len(lst)):
#    		print lst[i]
    		if col == lst[i] or abs(row - i) == abs(col - lst[i]):
    			return True
    	return False

    def NQueensRec(self, row, poslst, n, ret):
    	if row == n - 1:
    		for i in xrange(0, n):
    			if self.contradict(row, i, poslst) == False:
#    				print "yes"
    				matrix = []
    				for k in xrange(0, len(poslst)):
    					newrow = ""
    					for j in xrange(0, n):
    						if j == poslst[k]:
    							newrow += "Q"
    						else:
    							newrow += "."
    					matrix.append(newrow)
    				lastrow = ""
    				for j in xrange(0, n):
    					if j == i:
    						lastrow += "Q"
    					else:
    						lastrow += "."
    				matrix.append(lastrow)
    				ret.append(matrix)

    	else:
    		for i in xrange(0, n):
    			if self.contradict(row, i, poslst) == False:
    				poslst.append(i)
    				self.NQueensRec(row + 1, poslst, n, ret)
    				poslst.pop()


    def solveNQueens(self, n):
    	if n == 0:
    		return []
    	else:
    		ret = []
    		self.NQueensRec(0,[],n,ret)


    	return ret

s = Solution()
ret = s.solveNQueens(1)
print ret
        