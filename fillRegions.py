class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.


    def fillHole(self, board, visitedMap, row, col):
    	if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
    		return
    	visitedMap[i][j] = True
    	if board[i][j] == "O":
    		board[i][j] = "X"
    		self.fillHole(self, board, visitedMap, row - 1, col )
    		self.fillHole(self, board, visitedMap, row + 1, col)
    		self.fillHole(self, board, visitedMap, row, col - 1)
    		self.fillHole(self, board, visitedMap, row, col + 1)


    def solve(self, board):
        if board == None:
        	return board
        visitedMap = []
        for i in xrange (0 ,len(board)):
        	visitedMap[i] = []

        for i in xrange (0 ,len(board)):
        	lst = board[i]
        	for j in xrange (0, len(lst)):
        		visitedMap[i][j] = False


        for i in xrange (0 ,len (board)):
        	lst = board[i]
        	for j in xrange (0, len(lst)):
        		if visitedMap[i][j] == False:
        			if board[i][j] == "O":
        				self.fillHole(board,visitedMap,i,j)
        			visitedMap[i][j] = "X"


s = Solution()
s.solve (["X"])

