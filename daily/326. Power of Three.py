class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dummy = n

        if n <= 0: return False 

        while dummy > 0: 
            if dummy == 1: 
                return True
            if dummy % 3 == 0: 
                dummy /= 3
            else: 
                return False 
