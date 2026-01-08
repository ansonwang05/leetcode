"""
Docstring for 33. Search in Rotated Sorted Array

Easier solution would to be to do 2 binary searches on the array
First binary search would to be to find the pivot of the rotated array 
Second binary search would to be to search the where the target would lie according to the pivot 

Can do this either by writting a seperate binary serach function or just do 2 pass
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # still can't really wrap my head around it but it'll do for now
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = (left + right) // 2 

            if nums[mid] == target: 
                return mid
            if nums[mid] < nums[right]: 
                # pivot lies on the left side 
                if target < nums[mid] or target > nums[right]: 
                    # does the target lie on the left side 
                    # is the target smaller than then the mid or greater than the right
                    # continue binary search on the left side 
                    right = mid - 1
                else: 
                    left = mid + 1 
            else:
                # pivot lies on the right side
                if target > nums[mid] or target < nums[left]: 
                    # does the target lie on the right side 
                    # is the target greater than the mid or smaller than the left 
                    # continue binary search on the left side 
                    left = mid + 1 
                else: 
                    right = mid - 1 
        # not in the array 
        return -1 
        
