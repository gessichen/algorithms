class Solution:
    # @return a boolean

    def isLeftParren (self, c):
   		if c == '(' or c == '[' or c == '{':
   			return True
   		else:
   			return False

	def isMatch (c1,c2):
   		if (c1 == '{' and c2 = '}') or  (c1 == '[' and c2 = ']') or (c1 == '(' and c2 = ')'):
   			return True
   		else:
   			return False

    def isValid(self, s):
      	parentlst = []
      	l = len(s)
      	for x in xrange (0, l):
      		c = s[x]
      		if self.isLeftParren (c):
      			parentlst.append(c)
      		else:
      			if len (parentlst) == 0:
      				return False
      			lastc = parentlst.pop()
      			if lastc != c:
      				return False
      	if len (parentlst) > 0:
      		return False


s = Solution()
if s.isValid ('(){}'):
	print 'yes'
