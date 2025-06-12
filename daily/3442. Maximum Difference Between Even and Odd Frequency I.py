class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxDiff = maxOdd = 0
        minEven = 10 ** 6
        sArr = [0] * 26
        for i in range(len(s)):
            letter = s[i]
            index = ord(letter) - ord("a") 
            sArr[index] += 1

        for number in sArr: 
            if ((number % 2) == 1) and (maxOdd < number): 
                maxOdd = number
            if ((number % 2) == 0) and (minEven > number) and (number != 0): 
                minEven = number
        
        maxDiff = maxOdd - minEven
        return maxDiff
