'''
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):

    	if s1 == None or len(s1) == 0:
    		return s2 == s3
    	if s2 == None or len(s2) == 0:
    		return s1 == s3

    	if len(s1) + len(s2) != len(s3):
    		return False
    	c1 = s1[0]
    	c2 = s2[0]
    	c3 = s3[0]
    	ret = False
    	if c1 == c3:
    		ret = ret or self.isInterleave(s1[1:],s2,s3[1:])
    	if c2 == c3:
    		ret = ret or self.isInterleave(s1,s2[1:],s3[1:])

    	return ret
'''
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        isInterleaved = []
        if len(s3) != len(s1)+len(s2):
            return False
        for i in range(0,len(s1)+1):
            row = []
            for j in range(0,len(s2)+1):
                if i == 0 and  j==0:
                    row.append(True)
                else:
                    temp = False
                    if j>0: 
                        temp = row[j-1] and s3[i+j-1] == s2[j-1]
                    if i>0: 
                        temp = temp or (previousRow[j] and s3[i+j-1] == s1[i-1])
                    row.append(temp)
            previousRow = row
        return row[len(s2)]

s = Solution()

ret = s.isInterleave("aabcc","dbbca","aadbbbaccc")

print ret