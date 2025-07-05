class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        countDict = collections.Counter(arr)

        largest = -1
        for key, value in countDict.items(): 
            if key == value: 
                largest = max(largest, key)

        return largest
