class Solution(object):
    def runningSum(self, nums):
       runsum = []
       runsum.append(0)
       for num in nums:
            runsum.append(runsum[-1] + num)
       runsum.remove(0)
       return runsum
        