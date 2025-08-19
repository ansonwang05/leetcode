class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = occur = 0  
        for i in range(len(nums)): 
            if nums[i] == 0: 
                occur += 1
                result += occur
            else: 
                occur =  0 
            
        return result
