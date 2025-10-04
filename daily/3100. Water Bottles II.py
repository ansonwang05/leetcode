class Solution(object):
    # Solution is O(sqrt(n)), there is a way to optimize 
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
    
    # Optimize solution is O(1), using math
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int 
        :type numExchange: int
        :rtype: int
        """
        a = 1
        b = 2 * numExchange - 3
        c = -2 * numBottles
        delta = b * b - 4 * a * c
        t = int(math.ceil((-b + math.sqrt(delta))) / (2 * a))
        return numBottles

