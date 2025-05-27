class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        # Calculate Difference array
        differenceArray = [0] * (len(nums) + 1)
        for i in queries: 
            left = i[0]
            right = i[1] + 1
            differenceArray[left] += 1
            differenceArray[right] -= 1
        # Transform Difference array using Prefix Sum 
        for i in range(1, len(differenceArray)):
            differenceArray[i] = differenceArray[i-1] + differenceArray[i]
        # Compare whether or not the decrements allowed is sufficient to reach 0 for each nums[i]
        # Can be combined and done in one step ^ 
        for i in range(len(nums)): 
            if differenceArray[i] < nums[i]: 
                return False
        return True 
