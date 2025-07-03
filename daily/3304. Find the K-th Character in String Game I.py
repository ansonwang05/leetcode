class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = "a" 
        length = 1 
        while length < k: 
            length *= 2
            for i in range(len(word)): 
                curr = ord(word[i])
                word += (chr(curr+1))
        return word[k-1]
