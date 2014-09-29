class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
    	zeroRows = {}
    	zeroCols = {}

    	if matrix == None:
    		return matrix

    	for i in xrange (0, len(matrix)):
    		for j in xrange(0, len(matrix[0])):
    			if matrix[i][j] == 0:
    				if i not in zeroRows:
    					zeroRows[i] = True

    				if j not in zeroCols:
    					zeroCols[j] = True


    	for i in xrange (0, len(matrix)):
    		for j in xrange(0, len(matrix[0])):
    			if i in zeroRows or j in zeroCols:
    				matrix[i][j] = 0


