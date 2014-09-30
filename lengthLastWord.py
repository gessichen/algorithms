class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
    	if s == "":
    		return 0
    	newword = ""
    	oldword = ""
    	prev_c = ""
        for i in xrange(0, len(s)):
        	c = s[i]
        	if c != " ":
        		oldword = ""
        		newword += c
#        		print newword

        	else:
        		if prev_c != " ":
        			oldword = newword
        			newword = ""
        	prev_c = c
        if newword != "":
        	return len(newword)
        elif oldword != "":
        	return len(oldword)
        return 0


s = Solution()
ret = s.lengthOfLastWord("        ")

print ret