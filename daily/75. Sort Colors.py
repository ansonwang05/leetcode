class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numPairs = {}
        for i in nums:
            if i in numPairs:
                numPairs[i] += 1
            else:
                numPairs[i] = 1  
        curr = 0
        for i in range(len(numPairs)):
            currNum = numPairs.keys()[i]
            for j in range(numPairs[currNum]):
                nums[curr] = currNum
                curr += 1
            
