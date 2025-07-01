class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        numDict = {}
        for num in nums: 
            if num not in numDict: 
                numDict[num] = 1 
            else: 
                numDict[num] += 1
        
        for key in numDict.keys(): 
            diff = key + 1 
            if diff in numDict: 
                length = max(length, numDict[key] + numDict[diff])
        
        return length 
