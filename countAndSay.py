class Solution:
    # @return a string
    def countAndSay(self, n):
      	cnt = 1
      	s = "1"

      	while cnt != n:
      		subCnt = 0
      		cnts = []
      		chars = []
      		prev = ""
      		for i in xrange(0, len(s)):
      			c = s[i]
      			if prev == "":
      				subCnt += 1
      				chars.append(c)
      			else:
      				if c == prev:
      					subCnt += 1
      				else:
      					cnts.append(subCnt)
      					chars.append(c)
      					subCnt = 1
      			prev = c
      		cnts.append(subCnt)
      		s = ''
      		for i in xrange(0, len(cnts)):
      			s += str(cnts[i])
      			s += chars[i]
      		cnt += 1

      	return s

s = Solution()

ret = s.countAndSay(1)

print ret