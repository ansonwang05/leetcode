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
'''
Instead of running two for loops you can just run one for loop and check if the letter is in the the string s and the string t
An extra condition of this is that you have to check if the strings are now the same length, else you can iterate both strings the same time. 
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen = {}
        if len(s) != len(t): 
            return False
        for index in range(len(s)): 
            sLetter = s[index]
            tLetter = t[index] 
            if sLetter not in seen:
                seen[sLetter] = 1
            else: 
                seen[sLetter] += 1
            if tLetter not in seen: 
                seen[tLetter] = -1 
            else: 
                seen[tLetter] -= 1
        for key, value in seen.items():
            if value != 0: 
                return False
        return True
