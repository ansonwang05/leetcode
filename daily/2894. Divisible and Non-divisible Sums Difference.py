class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        sumDivisible = 0
        sumNotDivisible = 0
        for i in range(n + 1):
            if i % m == 0:
                sumDivisible += i
            else: 
                sumNotDivisible += i
        return sumNotDivisible - sumDivisible
