class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):

    	ret = []
        for i in xrange(len(s)-1,-1,-1):
        	print ret
       		ilst = []
       		j = i + 1
       		while  j < len(s) + 1:
       			if s[i:j] in dict:
#       				print "ok"
       				if j == len(s):
       					ilst.append(s[i:j])
       				else:
       					jlst = ret[len(s) - j - 1]
       					for k in xrange (0, len(jlst)):
       						sentence = jlst[k]
       						ilst.append (s[i:j] + " " + sentence)
       			j += 1
       		ret.append(ilst)
       	return ret[len(s) - 1]


st = "catsanddog"

dic = ["cats", "cat","sand","and","dog"];

s = Solution()

ret = s.wordBreak(st, dic)

print ret