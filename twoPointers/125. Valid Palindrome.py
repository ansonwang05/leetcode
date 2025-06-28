class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        frontP = 0 
        backP = len(s) - 1
        while frontP < backP: 
            frontL = s[frontP] 
            backL = s[backP] 
            if frontL.isalnum() and backL.isalnum():
                frontL = frontL.lower()
                backL = backL.lower()
                if frontL != backL: 
                    return False
                backP -= 1 
                frontP += 1
            elif frontL.isalnum(): 
                backP -= 1
            elif backL.isalnum():
                frontP += 1
            else:
                backP -= 1 
                frontP += 1
        return True 
                
