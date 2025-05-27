class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)):
            currNum = nums[index] 
            diff = target - currNum
            if diff in seen: 
                return [seen[diff], index]
            else:
                seen[currNum] = index 
            
