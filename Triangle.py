class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer

    def minimumTotal(self, triangle):
       	for i in xrange (len(triangle)-2, -1,-1):
       		for j in xrange (0, i):
       			triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])

       	return triangle[0][0]