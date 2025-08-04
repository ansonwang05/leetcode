class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maxFruits = left = 0 
        seenFruits = {}

        for i in range(len(fruits)): 
            if fruits[i] not in seenFruits:
                seenFruits[fruits[i]] = 1
            else: 
                seenFruits[fruits[i]] += 1 

            while len(seenFruits) > 2: 
                seenFruits[fruits[left]] -= 1
                if seenFruits[fruits[left]] == 0: 
                    del seenFruits[fruits[left]]
            
                left += 1 

            maxFruits = max(maxFruits, i - left + 1)

        return maxFruits

