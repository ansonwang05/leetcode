class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        differences = {}
        for i in range(len(nums)): 
            currNum = nums[i] 
            diff = target - currNum 
            if diff in differences: 
                return [differences[diff], i] 
            else: 
                differences[currNum] = i 
