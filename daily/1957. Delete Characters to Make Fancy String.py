class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s) 
        final = []
        counter = 0 
        prev = "A"

        for i in range(length):
            if prev == s[i]:  
                counter += 1
            else: 
                counter = 1 
                prev = s[i] 
            if counter < 3: 
                final.append(s[i])

        
        return "".join(final)
