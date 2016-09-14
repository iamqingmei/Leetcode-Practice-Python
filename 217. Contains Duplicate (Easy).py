"""
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
"""
class Solution(object):
    def containsDuplicate(self, nums): #42ms
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)
        if len(s)<len(nums):
            return True
        return False

    def containsDuplicate(self, nums): #207ms
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        if nums is None:
            return False
        for i in range (1,len(nums)):
            print (i)
            if (nums[i]==nums[i-1]):
                return True
        return False

