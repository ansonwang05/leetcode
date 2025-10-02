class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total = empty = numBottles 
        full = 0
        while (empty >= numExchange):
            empty -= numExchange
            full += 1
            empty += 1
            numExchange += 1
        return total + full
