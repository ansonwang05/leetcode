'''
In this problem we use a dictionary that has tuple as keys and an array as values
The keys are tuples because python dictionary requires keys to be immutable and arrays are mutable
The keys are tuples that are converted from array which keeps track of the ammount of letters in a word
    If a word has the same amount of letters as another word then it is a anagram otherwise it is not
The values are arrays that keep track of each word that is an anagram of another word
At the end we iterate through the dictionary to return all the arrays of anagrams appened to result
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        seen = {}
        for word in strs: 
            arrKey = [0] * 26
            for letter in word: 
                index = ord(letter) - ord("a")
                arrKey[index] += 1
            tupKey = tuple(arrKey)
            if tupKey not in seen:
                seen[tupKey] = [word]
            else: 
                seen[tupKey].append(word)
        for key, value in seen.items(): 
            result.append(value)
        return result
