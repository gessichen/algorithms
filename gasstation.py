class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        minval = float("inf")
        minPos = -1
        gasNow = 0

        for i in xrange (0, len(gas)):
            gasNow += (gas[i] - cost[i])
            if gas < minval:
                minval = gasNow
                minPos = i

        if gasNow >= 0:
            return (minPos + 1) % len(gas)
        return -1
        
s = Solution()

ret = s.canCompleteCircuit([5,6],[4,10])

print ret