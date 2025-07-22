class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        front = ans = 0 
        end = 1 
        total = nums[0] 
        seenDict = {nums[0] : 0}
        ans = max(ans, total)

        while end != len(nums): 
            total += nums[end]
            if nums[end] not in seenDict: 
                seenDict[nums[end]] = end
            else: 
                if seenDict[nums[end]] >= front: 
                    while nums[front] != nums[end]:
                        total -= nums[front] 
                        front += 1  
                    total -= nums[front]
                    front += 1
                seenDict[nums[end]] = end
            end += 1
            ans = max(ans, total)

        return ans
