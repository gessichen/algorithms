class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        boolcan = [1]
        length = len(A)
        print length
        j = 1
        while (j < length):
            print "j = " + str(j)
            boolcan.append(0)
            j += 1
            print "j = " + str(j) + "length = " + str(length)

        print str(boolcan)

        farest = 0
        for i in xrange(0,len(A)):
            if boolcan[i] == 1:
                if i == len(A) - 1:
					return True
                if (A[i] + i) > farest:
                    newfarest = A[i] + i
                    for i in xrange (farest + 1, newfarest + 1):
                        boolcan[i] = 1
                    farest = newfarest
        return False

s = Solution()
if s.canJump([2,3,1,1,4]):
	print "yes"