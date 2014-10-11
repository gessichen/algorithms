class Solution:
    # @return a string
    def findPrefix(self,str1, str2):
    	l1 = len(str1)
    	l2 = len(str2)
    	l = min(l1, l2)

    	i = 0
    	while i < l:
    		if str1[i] != str2[i]:
    			break;
    		i += 1

    	return str1[0:i]


    def longestCommonPrefix(self, strs):
    	if (strs == None or len(strs) == 0):
    		return ""

    	if (len(strs) == 1):
    		return strs[0]

    	base = strs[0]
    	i = 1
    	while i < len(strs):
    		compStr = strs[i]
    		prefix = self.findPrefix(base, compStr)
    		base = prefix
    		if base == "":
    			break
    		i += 1


    	return base

s = Solution()
ret = s.longestCommonPrefix(["ad"]);

print ret