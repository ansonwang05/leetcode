class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        table = {}
        numZeros = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0: 
                    table[numZeros] = (row, col)
                    numZeros += 1
        for key, value in table.items(): 
            row = value[0] 
            col = value[1]
            for rows in range(len(matrix)):
                for cols in range(len(matrix[rows])):
                    if row == rows:  
                        matrix[rows][cols] = 0
                    if col == cols: 
                        matrix[rows][cols] = 0

