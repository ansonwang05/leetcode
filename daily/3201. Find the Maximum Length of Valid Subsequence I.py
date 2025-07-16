class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        allEvens = allOdds = altEven = altOdd = 0 

        for i in range(len(nums)): 
            if nums[i] % 2: 
                allOdds += 1 
                altOdd = max(altOdd, altEven + 1)
            else: 
                allEvens += 1
                altEven = max(altEven, altOdd + 1)  

        return max(allOdds, allEvens, altOdd, altEven)
