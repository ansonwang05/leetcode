class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        sortNums = sorted(nums)

        for i in range(len(sortNums)): 
            if i > 0 and sortNums[i] == sortNums[i - 1]: 
                continue 
            
            left = i + 1
            right = len(sortNums) - 1 

            while left < right: 
                total = sortNums[left] + sortNums[right] + sortNums[i] 
                if total == 0: 
                    result.append([sortNums[i], sortNums[left], sortNums[right]])
                    left += 1 
                    right -= 1
                    while sortNums[left] == sortNums[left - 1] and left < right: 
                        left += 1
                elif total < 0: 
                    left += 1
                else: 
                    right -= 1
            
        return result 
