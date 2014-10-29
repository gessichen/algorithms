class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
    	lCnt = 0 
    	maxLen = 0
    	curLen = 0
    	lP = "("
    	rP = ")"

    	for i in xrange (0, len(s)):
    		c = s[i]
    		if c == rP:
    		    			

