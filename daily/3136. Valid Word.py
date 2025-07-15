class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word = word.lower()
        if len(word) < 3: 
            return False
        notAllowed = "@#$" 
        for char in notAllowed:
            if char in word: 
                return False 
        vowels = "aeiou" 
        hasVowel = hasConst = False
        for letter in word: 
            if letter.isalpha(): 
                if letter in vowels: 
                    hasVowel = True
                else: 
                    hasConst = True 
                if hasVowel == hasConst == True: 
                    return True
        return False

        
