class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
    	maxlen = 0
    	start = 0
    	dic = {}
        for i in xrange (0, len(s)):
        	c = s[i]
        	if dic.has_key (c):
        		pos = dic[c]
    #    		print 'pos' + ' ' + str(pos)
        		prevlen = i - start
    #    		print c + ' ' + str(prevlen)
        		if prevlen > maxlen:
        			maxlen = prevlen
        		
        		for key in dic.keys():
    #    			print str(start) + ' ' + str(dic[key]) + ' ' + str(pos)
        			if dic[key] >= start and dic[key] <= pos:
        				del dic[key]
       			dic[c] = i
    #    		print str(dic)
    			start = pos + 1
        	else:
        		dic[c] = i

        lastlen = len(s) - start
        if lastlen > maxlen:
        	maxlen = lastlen
        return maxlen

s = Solution()
ret = s.lengthOfLongestSubstring('wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco')
print str(ret)
