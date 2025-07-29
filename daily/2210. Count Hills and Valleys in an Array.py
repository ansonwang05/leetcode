class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        noDupe = [nums[0]] 
        hillValley = 0 
        while i != len(nums): 
            if nums[i] == nums[i - 1]: 
                i += 1
            else: 
                noDupe.append(nums[i]) 
                i += 1

        for i in range(1, len(noDupe) - 1): 
            prev = noDupe[i - 1]
            nex = noDupe[i + 1] 
            curr = noDupe[i] 
            if curr > prev and curr > nex: 
                hillValley += 1 
            elif curr < prev and curr < nex:
                hillValley += 1 
            
        return hillValley
