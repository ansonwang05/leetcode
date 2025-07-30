class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxNum = max(nums)
        maxSub = 1
        counter = 0 
        for i in range(nums.index(maxNum), len(nums)): 
            if nums[i] == maxNum: 
                counter += 1 
            else: 
                maxSub = max(maxSub, counter)  
                counter = 0

        return max(maxSub, counter)
