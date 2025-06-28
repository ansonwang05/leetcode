class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
# Not the optimal solution runtime of O(n^2) 
        result = [num for num in nums]
        while len(result) > k: 
            smallest = min(result) 
            result.remove(smallest)
        return result
