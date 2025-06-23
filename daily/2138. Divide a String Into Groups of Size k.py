class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        result = []
        front = 0
        back = k 
        numString = len(s) / k 
        for i in range(numString):
            substring = s[front:back] 
            result.append(substring)
            front += k 
            back += k
        if front == len(s): 
            return result
        last = s[front:]
        while len(last) < k: 
            last += fill
        result.append(last) 
        return result
