class Solution(object):
    # Already did ONCE in twoPointers 
    # Second Attempt
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = area = 0 
        right = len(height) - 1
        while left < right: 
            area = max(area, min(height[left], height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else: 
                left += 1
        return area