class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings

    def strWithOneSpace (self, words):
    	s = ''
    	for i in xrange (0, len(words) - 1):
    		s += words[i]
    		s += ' '
    	s += words[len(words) - 1]
    	return s

    def spreadSpacesOut(self,curwords,spacenum):
    	s = ''
    	if len(curwords) == 1:
    		print 'yes'
    		s = curwords[0]
    		for i in xrange (0, spacenum):
    			s += ' '
    		return s
    	slotssnum = len(curwords) - 1
    	basic = spacenum / slotssnum
    	numleft = spacenum % slotssnum
    #	print str(slotssnum) + ' ' + str(basic) + ' ' + str(numleft)
    	for i in xrange (0, slotssnum):
    #		print i 
    #		print 'gradual ' + s
    		s += curwords[i]
    		s += ' '
    		for j in xrange(0,basic):
    			s += ' '
    		if i < numleft :
    			s += ' '
    		print s
    	s += curwords[len(curwords) - 1]
   	#	print s + ' ' + str(len(s))
    	return s		
    				
    def appendWord(self, words, L, index, ret, curwords, originalL):
    #	print str(curwords)
    	if index == len(words):
    		print L
    		s = self.spreadSpacesOut(curwords,L + 1)
    		ret.append (s)
    		return
    	word = words[index]
#    	print 'word ' + word
    	if len(word) <= L:
    		curwords.append(word)
    		if len(word) == L:
    			print L
    			s = self.strWithOneSpace(curwords)
    			ret.append(s)
    		else:
    			self.appendWord (words, L - len(word) - 1, index + 1, ret, curwords,originalL)
    	else:
    		print 'going to spread out ' + str(curwords)
    		s = self.spreadSpacesOut(curwords,L + 1)
    		ret.append(s)
    		self.appendWord (words,originalL,index,ret,[],originalL)

    def fullJustify(self, words, L):
    	ret = []
    	self.appendWord (words, L, 0, ret, [], L)
       	return ret

s = Solution()
ret = s.fullJustify (["This", "is", "an", "example", "of", "text", "justification."], 16)
print str(ret)




        