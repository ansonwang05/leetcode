class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0 
        numsDict = collections.Counter(nums)
        maxFreq = max(numsDict.values())
        
        for value in numsDict.values(): 
            if value == maxFreq: 
                result += maxFreq

        return result 
