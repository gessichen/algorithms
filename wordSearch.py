class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    
    def existRec(self, board, word, row, col, index):
    	if index == len(word):
    		return True
    	if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
    		return False
    	if board[row][col] != word[index]:
    		return False

    	c = board[row][col]
#    	print c 
    	board[row][col] = "$"
    	ret = self.existRec(board, word, row + 1, col, index + 1) or self.existRec(board, word, row - 1, col, index + 1) or self.existRec(board, word, row, col + 1, index + 1) or self.existRec(board, word, row, col - 1, index + 1)

    	board[row][col] = c

    	return ret

    def exist(self, board, word):
    	if board == None:
    		return False

    	cboard = []
    	for i in xrange(0, len(board)):
    		cboard.append([])
    		for j in xrange(0, len(board[0][0])):
    			cboard[i].append(board[i][0][j])

#    	print cboard

    	for i in xrange(0, len(cboard)):
    		for j in xrange(0, len(cboard[0])):
    			if self.existRec(cboard,word,i,j,0):
    				return True

    	return False

s = Solution()
ret = s.exist([
  ["aa"],
], "aa")

print ret