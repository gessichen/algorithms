class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean

    def DFS (self, board, word, current, windex, hindex, boolboard):
    	if word[0:len(current)] != current:
    		return False
    	if len(current) == len (word):
    		return True
    	
    	if windex >= len(board[0][0]) or hindex >= len(board):
    		return False
    	boolboard[hindex][windex] = True
    	print current + board[hindex][0][windex]
    	boolleft = windex - 1 >= 0 and boolboard[hindex][windex - 1] == False and self.DFS(board,word,current + board[hindex][0][windex], windex - 1, hindex, boolboard)
    	if boolleft:
    		return True
    	boolright = windex + 1 < len(board[0][0]) and boolboard[hindex][windex + 1] == False and self.DFS(board,word,current + board[hindex][0][windex], windex + 1, hindex, boolboard) 
    	if boolright:
    		return True
    	boolup = hindex - 1 >= 0 and boolboard[hindex - 1][windex] == False and self.DFS(board,word,current + board[hindex][0][windex], windex, hindex - 1, boolboard)
    	if boolup:
    		return True 
    	booldown = hindex + 1 < len(board) and boolboard[hindex + 1][windex] == False and self.DFS(board,word,current + board[hindex][0][windex], windex, hindex + 1, boolboard)
    	if booldown:
    		return True
    	else:
    		boolboard[hindex][windex] == False
    		return False


    def exist(self, board, word):	
        if len (board) == 0 or len(word) == 0:
        	return False
       	boolboard = []
       	h = len(board)
       	w = len(board[0][0])
#       	print str(h) + ' ' + str(w)
       	for i in xrange (0, h):
       		boolboard.append([])
       		for j in xrange (0, w):
       			boolboard[i].append(False)
#       	print str(boolboard)
       	for i in xrange (0, h):
       		for j in xrange (0, w):
       			if board[i][0][0] == word[0]:
       				if self.DFS(board, word, '', i, j, boolboard):
       					return True
       	return False

       				

s = Solution()
if s.exist([["ABCE"],["SFCS"],["ADEE"]], "ABCB"):
	print "Yes"

