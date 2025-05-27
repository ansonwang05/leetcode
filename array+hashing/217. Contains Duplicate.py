'''
Solution A: 
  Python's unique data structure, sets, are unorderd, unchangeable, and unindexed. They also have the special property of not allowing duplicate values. 
  This solution requires that it returns false if there are no duplicates and true if there are duplicates. 
  We take the list nums and convert it to a set therefore getting rid of all the duplicate values.
  So if we take the initial length of the list and subtract it with the length of the set, we will get 0 which means that there are no duplicates or a number > 0 which means there are duplicates. 
  We compare the subtraction to 0, if it is not 0 we return true, and if it is zero we return false. 
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lengthNums = len(nums)
        lengthSet = len(set(nums))
        return (lengthNums - lengthSet) != 0 
'''
Solution B:
  More intuitive, we are iterating through the array and seeing if any values are repeated. If the value is repeated then we return true because there is a duplicate, otherwise we return false. 
  We can store these values in a hashmap where all keys are unique and values can be repeated. 
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for number in nums:
            if number in seen:
                return True
            else:
                seen[number] = 1
        return False 
