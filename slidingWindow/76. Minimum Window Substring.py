class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        require = collections.Counter(t) 
        left = right = 0 
        smallest = 10 ** 5  

        while right < len(s):
            if s[right] in require: 

                require[s[right]] -= 1 
                
                while require.values() == ([0] * (len(t))): 
                    smallest = min(smallest, right - left + 1) 
                    if s[left] in require: 
                        require = collections.Counter(t)
                    left += 1

            right += 1 


        print(smallest)
