"""
First solution is simple sliding window, a set is created to keep track of the seen characters in the string
Window is shortened until the duplicate character doesn't exist in the set
Adds the current letter to the set after removing duplicates 
Length is calcuated by taking the right pointer - left pointer + 1 to account inclusive 
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seenSet = set() 
        left = longest = 0 

        for right in range(len(s)): 
            while s[right] in seenSet: 
                seenSet.remove(s[left])
                left += 1 
            seenSet.add(s[right]) 
            longest = max(longest, right - left + 1)

        return longest 

"""
Second solution is also sliding window, a dictionary is created to keep track of the indicies of the characters in the string 
Window is 'shortedned' by setting the value of the left side to be one more than the previous index of the existing value 
Its current index will be updated afterwards and the longes window will be calculated the same way 
"""
        
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seenDict = {}
        left = longest = 0 

        for i in range(len(s)): 
            if s[i] in seenDict: # If it is already in the dictionary then it had already been seen 
                left = max(seenDict[s[i]] + 1, left) # Keep the left pointer updated to not included the duplicate character 

            seenDict[s[i]] = i # Update the indicies of the values of each character
            longest = max(longest, i - left + 1) # Calculate the longest of the window 
        
        return longest 
