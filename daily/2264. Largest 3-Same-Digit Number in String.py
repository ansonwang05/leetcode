class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        potential = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"] 

        for trio in potential:
            if trio in num:
                return trio 
        
        return "" 


