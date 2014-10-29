class Solution:
    # @return an integer
    def numDistinct(self, S, T):
   		if len(S) < len(T):
   			return 0 
   		elif len(S) == len(T) and S == T:
   			return 1 

   		else:
   			prevRow = None
   			for i in xrange (0, len(T)):
   				newRow = []
   				for j in xrange(0, len(S)):
   					num = 0
   					if S[j] == T[i]:
   						if i == 0 and j == 0:
   							num = 1
   						else:
   							if i == 0:
   								num = newRow[j-1] + 1
   							elif j == 0:
   								num = 0
   							else:
   								num = newRow[j-1] + prevRow[j-1]
   					else:
   						if j == 0:
   							num = 0
   						else:
   							num = newRow[j-1]

   					newRow.append(num)
   				prevRow = newRow
   			return newRow[len(S)-1]


s = Solution()

ret = s.numDistinct("ccc", "c")

print ret