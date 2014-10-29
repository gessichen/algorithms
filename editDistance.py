class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
    	if word1 == "":
    		return len(word2)
    	if word2 == "":
    		return len(word1)


    	prevRow = None
    	for i in xrange (0 ,len(word1)):
    		newRow = []
    		add = 0
    		for j in xrange(0, len(word2)):
    			if word1[i] == word2[j]:
    				add = 0
    			else:
    				add = 1
    			if i == 0 and j == 0:
    				newRow.append(0)
    			elif i == 0:
    				if newRow[j-1] < j:
    					newRow.append(newRow[j-1] + 1)
    				else:
    					newRow.append(newRow[j-1] + add)
    			elif j == 0:
    				if prevRow[i-1] < i:
    					newRow.append(prevRow[i-1] + 1)
    				else:
    					newRow.append(prevRow[i-1] + add)
    			else:
    				newRow.append(min((prevRow[j]+1),(newRow[j-1]+1),(prevRow[j-1]+add)))
    		prevRow = newRow

    	return prevRow[len(word2) - 1]


s = Solution()

ret = s.minDistance("eat","ate")

print ret