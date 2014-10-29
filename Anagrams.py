class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):

    	strMap = {}
    	ret = []
    	for i in xrange (0, len(strs)):
    		s = strs[i]
    		charArr = list(s)
    		charArr.sort()
    		keyStr = ""

    		for j in xrange(0, len(charArr)):
    			keyStr += charArr[j]
    		if keyStr in strMap:
    			if strMap[keyStr] != None:
    				ret.append(strMap[keyStr])
    				ret.append(s)
    				strMap[keyStr] = None

    			else:
    				ret.append(s)

    		else:
    			strMap[keyStr] = s

    	return ret

s = Solution()

ret = s.anagrams(["abc","bca","dd","bac"])

print ret
