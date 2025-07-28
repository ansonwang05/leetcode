class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        if max(nums) < 0: 
            return max(nums) 
        numSet = set(nums)
        for num in numSet: 
            if num > 0: 
                total += num
        return total 
