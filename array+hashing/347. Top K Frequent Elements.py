class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        result = []
        for num in nums: 
            if num not in freq: 
                freq[num] = 1
            else:
                freq[num] += 1
        freqList = sorted(list(freq.items()), key=lambda x: x[1], reverse=True)
        if len(freqList) == 1: 
            result.append(freqList[0][0])
            return result
        for i in range(k): 
            result.append(freqList[i][0])
        return result
