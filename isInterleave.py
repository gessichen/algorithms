class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
    	print s1
    	print s2
    	print s3
    	print '########'

        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l1 + l2 != l3:
        	return False

        ret = False
        firstway = False
        secondway = False

        if l1 == 0:
        	if s2 == s3:
        		ret = True

        elif l2 == 0:
        	if s1 == s3:
        		ret = True

        if l1 > 0 and s1[0] == s3[0]:
        	print 'firstway' + ':' + s1[1:] + ' ' + s2 + ' ' + s3[1:]
        	firstway = self.isInterleave(s1[1:], s2, s3[1:])
        	if 	firstway == True:
        		ret = True

#        print 'secondway:' + s1 + ' ' + s2 + ' ' + s3

        elif firstway == False and l2 > 0 and s2[0] == s3[0]:
			print 'entered secondway'
            secondway = self.isInterleave(s1, s2[1:], s3[1:])
        	if secondway == True:
        		ret = True

       	return ret

s = Solution()
if s.isInterleave('aabcc','dbbca','aadbbcbcac'):
	print 'yes'