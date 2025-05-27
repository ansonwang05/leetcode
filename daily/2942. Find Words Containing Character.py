class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        indices = []
        for i in range(len(words)):
            if x in words[i]:
                indices.append(i)
        return indices
