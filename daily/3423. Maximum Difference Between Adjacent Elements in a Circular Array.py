class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxDiff = 0
        for i in range(1, len(nums)): 
            diff = abs(nums[i] - nums[i-1])
            if maxDiff < diff: 
                maxDiff = diff
        edge = abs(nums[len(nums) - 1] - nums[0])
        if maxDiff < edge:
            maxDiff = edge
        return maxDiff
