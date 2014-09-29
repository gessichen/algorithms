class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        startToEnd = {}
        endToStart = {}

        longest = 0

        for i in xrange (0, len(num)):

            cur_num = num[i]
            start = cur_num
            end = cur_num


#            print cur_num

            if cur_num in startToEnd:
                end = startToEnd[cur_num]
                del startToEnd[cur_num]
                del endToStart[end]

            if cur_num in endToStart:
                start = endToStart[cur_num]
                del endToStart[cur_num]
                del startToEnd[start]

            if cur_num + 1 in startToEnd:
                hisend = startToEnd[cur_num + 1]
                end = max(hisend,end)
                del startToEnd[cur_num + 1]
                del endToStart[hisend]


            if cur_num - 1 in endToStart:
                hisstart = endToStart[cur_num - 1]
                start = min(hisstart,start)
                del endToStart[cur_num - 1]
                del startToEnd[hisstart]

            longest = max(longest, end - start + 1)

            startToEnd[start] = end
            endToStart[end] = start

#            print "start:" + str(start) + " " + "end:" + str(end)

        return longest

s = Solution()

ret = s.longestConsecutive([-6,8,-5,7,-9,-1,-7,-6,-9,-7,5,7,-1,-8,-8,-2,0])

print ret
