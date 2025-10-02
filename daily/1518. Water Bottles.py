class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
        total = exchangeable = numBottles 
        while (exchangeable >= numExchange):     
            total += exchangeable // numExchange 
            exchangeable = exchangeable // numExchange + exchangeable % numExchange
        return total 
