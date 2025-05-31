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
