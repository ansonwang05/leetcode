class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1, numRows + 1): 
            currRow = [1] * i 
            if i > 2: 
                for j in range(1, len(currRow) - 1): 
                    currRow[j] = result[i - 2][j - 1] + result[i - 2][j]
            result.append(currRow)

        return result 
