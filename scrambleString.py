class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
    	l1 = len(s1)
    	l2 = len(s2)

    	if l1 != l2:
    		return False

    # if there is only one character just check thet are the same	
    	if s1 == s2:
#    		print "--------------"
#    		print s1 
#    		print s2 
    		return True

    	sum1 = 0
    	sum2 = 0

    	for i in xrange(0, l1):
    		sum1 += ord(s1[i])
    		sum2 += ord(s2[i])

#    	print "************"
#    	print s1 + " " + str(sum1) 
#    	print s2 + " " + str(sum2)
    	if sum2 != sum1:
#    		print "here"
    		return False
#    	print "same"
    	ret = False
    	for i in xrange(1,l1):
    		if ( (self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:l1],s2[i:l1])) or (self.isScramble(s1[0:i],s2[l1-i:l1]) and self.isScramble(s1[i:l1],s2[0:l1-i]))):
    			return True
#    	print "return final"
    	return ret
s = Solution()
ret = s.isScramble("abc","bca")

print ret 
 

