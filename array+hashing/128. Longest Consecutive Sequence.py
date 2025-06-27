class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# First Try using sorting which is O(n log n) not very efficient
        if len(nums) == 0: 
            return 0

        consec = []
        currSeq = 1
        sortNum = sorted(nums)
        for i in range(1, len(sortNum)):
            currNum = sortNum[i]
            prevNum = sortNum[i - 1] 
            if currNum - 1 == prevNum: 
                currSeq += 1 
            elif currNum == prevNum: 
                continue
            else: 
                consec.append(currSeq)
                currSeq = 1
        consec.append(currSeq)
        return max(consec)
