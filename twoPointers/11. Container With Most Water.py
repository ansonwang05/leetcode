class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0 
        right = len(height) - 1

        result = 0 

        while left < right: 
            width = right - left
            if height[left] < height[right]: 
                result = max(result, height[left] * width)
                left += 1
            else: 
                result = max(result, height[right] * width)
                right -= 1
            
        return result
