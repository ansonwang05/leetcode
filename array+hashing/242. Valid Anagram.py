class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen = {}
        for letter in s: 
            if letter not in seen: 
                seen[letter] = 1
            else:
                seen[letter] += 1
        for letter in t:
            if letter in seen: 
                seen[letter] -= 1
            else:
                return False
        for key, value in seen.items():
            if value != 0:
                return False
        return True
