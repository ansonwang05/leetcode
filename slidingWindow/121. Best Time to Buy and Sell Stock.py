class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = highest = 0 
        lowest = prices[0] 
        for price in prices: 
            if price < lowest: 
                lowest = price 
                highest = 0 
            elif price > highest: 
                highest = price 
                profit = max(profit, highest - lowest)

        return profit

