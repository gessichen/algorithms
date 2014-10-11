class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        l1 = len(a)
        l2 = len(b)

        if l1 > l2:
        	for i in xrange (0, l1-l2):
        		b = "0" + b
        elif l2 > l1:
        	for i in xrange (0, l2-l1):
        		a = "0" + a
        l = max(l1,l2)

        levelUp = 0
        s = ''
        for i in xrange(l-1,-1,-1):
        	aci = int(a[i])
        	bci = int(b[i])

        	r = (aci + bci + levelUp) % 2
        	levelUp = (aci + bci + levelUp) / 2

        	s = str(r) + s

       	if levelUp == 1:
       		s = "1" + s

       	return s


s = Solution()
ret = s.addBinary("1","1")

print ret




